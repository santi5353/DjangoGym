from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookingForm, ContactoForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Instructor, Routine, Booking
from django.db import IntegrityError
from memberships.models import Membresia
from services.models import Servicio


# Vista de la página principal (Home)
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['membresias'] = Membresia.objects.filter(activo=True)
        context['servicios'] = Servicio.objects.filter(activo=True)
        return context

    def post(self, request, *args, **kwargs):
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            try:
                send_mail(
                    f'Mensaje de {nombre} - {asunto}',
                    mensaje,
                    email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, '¡Gracias por contactarnos, nos comunicaremos pronto contigo!')
            except Exception as e:
                messages.error(request, f'Error al enviar el correo: {str(e)}')

            return self.render_to_response(self.get_context_data(form=ContactoForm()))  # Redirige con el formulario vacío
        return self.render_to_response(self.get_context_data(form=form))  # En caso de error, vuelve a cargar el formulario


# Vista para el registro de un usuario
class UserSignupView(CreateView):
    template_name = 'signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup')  # Redirige a la misma página en caso de éxito, pero no es necesario para nuestro caso.

    def form_valid(self, form):
        user = form.save()  # Guarda el usuario
        login(self.request, user)  # Inicia sesión automáticamente
        messages.success(self.request, '¡Registro exitoso! Bienvenido.')
        
        # Devuelve el mismo template con el mensaje de éxito
        return render(self.request, self.template_name, {'form': form, 'success': True})

    def form_invalid(self, form):
        messages.error(self.request, 'Error en el registro. Verifica los datos.')
        return render(self.request, self.template_name, {'form': form, 'success': False})

# Vista para el login de un usuario
class UserLoginView(LoginView):
    template_name = 'signin.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        messages.success(self.request, '¡Inicio de sesión exitoso!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')  # Redirige al home después de iniciar sesión

    def form_invalid(self, form):
        messages.error(self.request, 'Nombre de usuario o contraseña incorrectos.')
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    next_page = '/'  # Redirige al home después de cerrar sesión

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Has cerrado sesión.')
        return super().dispatch(request, *args, **kwargs)


# Vista de bienvenida o página de éxito después de login/signup
class WelcomeView(TemplateView):
    template_name = 'users/welcome.html'


# Vista para listar instructores (requiere autenticación)
class InstructorListView(LoginRequiredMixin, ListView):
    model = Instructor
    template_name = 'instructors.html'
    context_object_name = 'instructors'


# Vista para listar rutinas (requiere autenticación)
class RoutineListView(LoginRequiredMixin, ListView):
    model = Routine
    template_name = 'routines.html'
    context_object_name = 'routines'


# Vista para crear una reserva (requiere autenticación)
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'create_booking.html'
    success_url = reverse_lazy('my_bookings')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Asigna el usuario autenticado
        return super().form_valid(form)


# Vista de éxito para la creación de una reserva
class BookingSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'booking_success.html'


# Vista para mostrar las reservas del usuario (requiere autenticación)
class MyBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'my_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

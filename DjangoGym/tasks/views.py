from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import BookingForm, ContactoForm
from .models import Instructor, Routine, Booking, Membresia, Servicio
import logging


# Home view that renders active memberships
# Configuración básica de logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def home(request):
    membresias = Membresia.objects.filter(activo=True)
    servicios = Servicio.objects.all()

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Obtener datos del formulario
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            # Intentar enviar el correo
            try:
                send_mail(
                    f'Mensaje de {nombre} - {asunto}',
                    mensaje,
                    email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                # Agregar mensaje de éxito
                messages.success(request, '¡Gracias por contactarnos, nos comunicaremos pronto con tigo!')
            except Exception as e:
                # Agregar mensaje de error
                messages.error(request, f'Error al enviar el correo,: {str(e)}')

            # Redirigir a la misma página con el formulario vacío después de enviar el mensaje
            return render(request, 'home.html', {
                'membresias': membresias,
                'servicios': servicios,
                'form': ContactoForm()  # Formulario vacío después del envío
            })
    else:
        form = ContactoForm()

    return render(request, 'home.html', {
        'membresias': membresias,
        'servicios': servicios,
        'form': form
    })
# Signup view for new users
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                login(request, user)
                return redirect('home')  # Redirect to home after successful signup
            except IntegrityError:
                return render(request, 'signup.html', {
                    "form": UserCreationForm(),
                    "error": "El nombre de usuario ya existe. Por favor, elige otro.",
                })
        return render(request, 'signup.html', {
            "form": UserCreationForm(),
            "error": "Las contraseñas no coinciden.",
        })

# Sign-in view
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('home')  # Redirect to home or a protected page

# Sign-out view
@login_required
def signout(request):
    logout(request)
    return redirect('home')

# Instructor list view
@login_required
def instructors(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructors.html', {"instructors": instructors})

# Routine list view
@login_required
def routines(request):
    routines = Routine.objects.all()
    return render(request, 'routines.html', {"routines": routines})

# Booking creation view
@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assign the authenticated user
            booking.save()
            return redirect('my_bookings')
    else:
        form = BookingForm()

    return render(request, 'create_booking.html', {'form': form})

# Booking success page
@login_required
def booking_success(request):
    return render(request, 'booking_success.html')

# Display the user's bookings
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})


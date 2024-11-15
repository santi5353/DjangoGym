from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Instructor, Routine,  Booking
from django.contrib.auth.decorators import login_required


# from .forms import TaskForm

# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # Crear el usuario
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                # Iniciar sesión automáticamente (opcional)
                login(request, user)
                # Enviar mensaje de éxito
                return render(request, 'signup.html', {
                    "form": UserCreationForm(),
                    "success": "¡Registro exitoso! Ahora puedes comenzar a usar la aplicación.",
                })
            except IntegrityError:
                return render(request, 'signup.html', {
                    "form": UserCreationForm(),
                    "error": "El nombre de usuario ya existe. Por favor, elige otro.",
                })

        # Manejo de error si las contraseñas no coinciden
        return render(request, 'signup.html', {
            "form": UserCreationForm(),
            "error": "Las contraseñas no coinciden.",
        })


# @login_required
# def tasks(request):
#     tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
#     return render(request, 'tasks.html', {"tasks": tasks})


# @login_required
# def tasks_completed(request):
#     tasks = Task.objects.filter(
#         user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
#     return render(request, 'tasks.html', {"tasks": tasks})


# @login_required
# def create_task(request):
#     if request.method == "GET":
#         return render(request, 'create_task.html', {"form": TaskForm})
#     else:
#         try:
#             form = TaskForm(request.POST)
#             new_task = form.save(commit=False)
#             new_task.user = request.user
#             new_task.save()
#             return redirect('tasks')
#         except ValueError:
#             return render(request, 'create_task.html', {"form": TaskForm, "error": "Error creating task."})


def home(request):
    return render(request, 'home.html')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('create_booking')


# @login_required
# def task_detail(request, task_id):
#     if request.method == 'GET':
#         task = get_object_or_404(Task, pk=task_id, user=request.user)
#         form = TaskForm(instance=task)
#         return render(request, 'task_detail.html', {'task': task, 'form': form})
#     else:
#         try:
#             task = get_object_or_404(Task, pk=task_id, user=request.user)
#             form = TaskForm(request.POST, instance=task)
#             form.save()
#             return redirect('tasks')
#         except ValueError:
#             return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task.'})


# @login_required
# def complete_task(request, task_id):
#     task = get_object_or_404(Task, pk=task_id, user=request.user)
#     if request.method == 'POST':
#         task.datecompleted = timezone.now()
#         task.save()
#         return redirect('tasks')


# @login_required
# def delete_task(request, task_id):
#     task = get_object_or_404(Task, pk=task_id, user=request.user)
#     if request.method == 'POST':
#         task.delete()
#         return redirect('tasks')

@login_required
def instructors(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructors.html', {"instructors": instructors})


@login_required
def routines(request):
    routines = Routine.objects.all()
    return render(request, 'routines.html', {"routines": routines})

@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Asigna el usuario autenticado
            booking.save()
            return redirect('my_bookings')  # Redirige a la vista de reservas después de la creación
    else:
        form = BookingForm()

    return render(request, 'create_booking.html', {'form': form})


@login_required
def booking_success(request):
    return render(request, 'booking_success.html')


@login_required
def my_bookings(request):
    # Obtener las reservas del usuario actual
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})

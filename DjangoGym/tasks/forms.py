from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# Formulario para crear una reserva
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ["instructor", "routine", "class_date"]
        widgets = {
            "class_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),  # Formato para datetime-local
        }

# Formulario de contacto
class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label="Nombre",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Tu nombre"}
        ),
    )
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Tu correo electrónico"}
        ),
    )
    asunto = forms.CharField(
        max_length=200,
        label="Asunto",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Asunto del mensaje"}
        ),
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Escribe tu mensaje aquí",
            }
        ),
    )

# Formulario de creación de usuario personalizado
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Tu nombre de usuario"})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Tu contraseña"})
    )
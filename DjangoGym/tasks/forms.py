from django import forms
from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ["instructor", "routine", "class_date"]
        widgets = {
            "class_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


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

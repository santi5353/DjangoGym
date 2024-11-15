from django import forms
from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['instructor', 'routine', 'class_date']
        widgets = {
            'class_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

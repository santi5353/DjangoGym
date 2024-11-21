from django.contrib import admin
from .models import Membresia

@admin.register(Membresia)
class MembresiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'activo')

from django.contrib import admin
from .models import Instructor, Routine, Booking,  Membresia, Servicio

# Register your models here.

# class TaskAdmin(admin.ModelAdmin):
#     readonly_fields = ('created', )

# admin.site.register(Task, TaskAdmin)


@admin.register(Membresia)
class MembresiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'duracion', 'precio', 'activo')  # Campos a mostrar en la lista
    search_fields = ('nombre', 'descripcion')  # Campos por los cuales se puede buscar
    list_filter = ('activo',)  # Filtro por el campo 'activo'
    ordering = ('nombre',)  # Ordenar por el campo 'nombre'

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'activo')

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty')
    search_fields = ('name', 'specialty')

# Ya no necesitas registrar nuevamente el modelo Instructor aquí
# admin.site.register(Instructor)


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration_minutes', 'instructor')
    list_filter = ('instructor',)
    search_fields = ('name', 'instructor__name')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'instructor', 'routine',
                    'class_date', 'date_booked')
    list_filter = ('instructor', 'routine')
    search_fields = ('user__username', 'instructor__name', 'routine__name')

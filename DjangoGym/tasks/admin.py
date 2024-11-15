from django.contrib import admin
from .models import Instructor, Routine, Booking

# Register your models here.

# class TaskAdmin(admin.ModelAdmin):
#     readonly_fields = ('created', )

# admin.site.register(Task, TaskAdmin)


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

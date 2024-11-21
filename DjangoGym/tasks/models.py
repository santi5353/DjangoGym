from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.



class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Routine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration_minutes = models.PositiveIntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    routine = models.ForeignKey('Routine', on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)
    class_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} - {self.instructor.name} - {self.routine.name}'

from django.db import models







from django.db import models

class Membresia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField(help_text="Duración en días")
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    activo = models.BooleanField(default=True)
    beneficios = models.JSONField(default=list, blank=True, help_text="Lista de beneficios de la membresía")

    def __str__(self):
        return self.nombre

# Generated by Django 5.1.3 on 2024-11-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('duracion', models.IntegerField(help_text='Duración en días')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('activo', models.BooleanField(default=True)),
                ('beneficios', models.JSONField(blank=True, default=list, help_text='Lista de beneficios de la membresía')),
            ],
        ),
    ]

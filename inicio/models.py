from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre_de_usuario = models.CharField(max_length=50, unique=True)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    puntuacion_python = models.IntegerField(default=0)
    puntuacion_c_mas_mas = models.IntegerField(default=0)
    puntuacion_golang = models.IntegerField(default=0)

    preguntas_respondidas = models.IntegerField(default=0)

    url = models.URLField(null=True)
    sobre_mi = models.TextField(null=True)

    def __str__(self):
        return self.nombre_de_usuario

from django.db import models
from empreza.models import Empreza

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    correo_electronico = models.CharField(max_length=25)
    edad = models.IntegerField()
    numero_empleado = models.IntegerField()
    dirrecion = models.CharField(max_length=40)
    empreza_matrix = models.ManyToManyField(Empreza)



    
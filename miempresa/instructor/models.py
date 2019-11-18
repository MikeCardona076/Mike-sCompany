from django.db import models
from alumno.models import Alumno
#from curso.models import Curso

# Create your models here.
class Instructor(models.Model):
    cedula_profesional = models.CharField(max_length=30)
    carrera = models.CharField(max_length=30)
    nombre_instructor = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)

    matrix = models.ManyToManyField(Alumno)
    #curso_matrix = models.ManyToManyField(Curso)


     




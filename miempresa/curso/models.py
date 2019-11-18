from django.db import models
from instructor.models import Instructor

# Create your models here.
class Curso(models.Model):
     tipo_curso = models.CharField(max_length=30)
     titulo_curso = models.CharField(max_length=30)
     fecha_inicio = models.DateField()
     fecha_fin = models.DateField()
     numero_curso = models.IntegerField()
     duracion = models.IntegerField( )
     curso_profesor = models.ManyToManyField(Instructor)
     



from django.db import models

# Create your models here.
class Empreza(models.Model):
    nombre_empresa = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    rfc = models.CharField(max_length=30)




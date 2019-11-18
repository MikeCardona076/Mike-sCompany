from django.contrib import admin
from .models import Alumno

# Register your models here.
#admin.site.register(Cliente)

@admin.register(Alumno)

class AlumnoAdmin(admin.ModelAdmin):
    list_display = [
    "nombre",
    "telefono",
    "numero_empleado"
    ]
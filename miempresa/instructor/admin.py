from django.contrib import admin

from .models import Instructor

# Register your models here.
#admin.site.register(Cliente)

@admin.register(Instructor)

class InstructorAdmin(admin.ModelAdmin):
    list_display = [
    "nombre_instructor",
    "carrera",
    "telefono"
    ]
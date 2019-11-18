from django.contrib import admin

from .models import Curso

# Register your models here.
#admin.site.register(Cliente)

@admin.register(Curso)

class CursoAdmin(admin.ModelAdmin):
    list_display = [
    "tipo_curso",
    "fecha_inicio",
    "fecha_fin"
    ]
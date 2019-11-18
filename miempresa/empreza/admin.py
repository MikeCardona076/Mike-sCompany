from django.contrib import admin

from .models import Empreza

# Register your models here.
#admin.site.register(Cliente)

@admin.register(Empreza)

class EmprezaAdmin(admin.ModelAdmin):
    list_display = [
    "nombre_empresa",
    "telefono",
    "rfc"
    ]
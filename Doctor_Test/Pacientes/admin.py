from django.contrib import admin

from .models import Paciente



# Register your models here.
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display= ('documento', 'nombre', 'apellido','eps','telefono')
    list_filter =('documento','nombre','apellido')




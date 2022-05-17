from django.contrib import admin

from .models import Paciente, historia, diagnostico



# Register your models here.
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display= ('documento', 'nombre', 'apellido','eps','telefono')
    list_filter =('documento','nombre','apellido')
    
@admin.register(historia)
class historiaAdmin(admin.ModelAdmin):
    list_display= ('id','paciente_id')
    list_filter =('id',)

@admin.register(diagnostico)
class diagnosticoAdmin(admin.ModelAdmin):
    list_display= ('id',)
    



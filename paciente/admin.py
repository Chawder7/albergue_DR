from django.contrib import admin
from .models import Paciente
# Register your models here.

class administrarPaciente(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombrePaciente','apellidoPaciente','edad','genero')
    
    
admin.site.register(Paciente, administrarPaciente)

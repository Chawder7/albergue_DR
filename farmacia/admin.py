from django.contrib import admin
from .models import Medicamentos

# Registro del modelo de medicamentos
class AdministrarMedicamento(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'nombreMed', 'categoria','cantidad')
    
admin.site.register(Medicamentos, AdministrarMedicamento)

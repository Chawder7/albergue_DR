from django.contrib import admin
from .models import Receta
# Register your models here.

class administrarReceta(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('paciente','doctor','diagnostico', 'medicamento')
    
    
admin.site.register(Receta, administrarReceta)
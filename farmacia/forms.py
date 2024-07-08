from django import forms
from .models import Medicamentos
from django.forms import ModelForm, ClearableFileInput

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for = "%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'
class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamentos
        fields = ('nombreMed', 'categoria', 'cantidad', 'fechaVen', 'descripcion')
        widgets = {
            'fotoMed': CustomClearableFileInput
        }
        




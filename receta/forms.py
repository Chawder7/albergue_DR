from django import forms
from .models import Receta
from django.forms import ModelForm, ClearableFileInput
class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for = "%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'
class RecetaForm(ModelForm):
    class Meta:
        model = Receta
        fields = ('paciente', 'doctor', 'diagnostico', 'medicamento', 'cantidad')
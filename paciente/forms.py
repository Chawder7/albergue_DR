from django import forms
from .models import Paciente
from django.forms import ModelForm, ClearableFileInput

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for = "%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'
class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ('nombrePaciente', 'apellidoPaciente', 'edad', 'genero', 'fotoPaciente')
        widgets = {
            'fotoPaciente': CustomClearableFileInput
        }
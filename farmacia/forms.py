from django import forms
from .models import Medicamentos

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamentos
        fields = ['nombreMed', 'categoria', 'cantidad', 'fechaVen', 'descripcion', 'fotoMed']
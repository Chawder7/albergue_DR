from django.shortcuts import render
from django.db.models import Count
from .models import Paciente
from receta.models import Receta

# Create your views here.
def pacientes(request):
    pacientes =  Paciente.objects.annotate(num_recetas=Count('receta')).only("id","nombrePaciente","apellidoPaciente","edad","genero")
    return render(request, "paciente/viewPaciente.html",{'pacientes':pacientes})

def pacienteDetalles(request):
    return render(request, "paciente/viewPacienteInfo.html")
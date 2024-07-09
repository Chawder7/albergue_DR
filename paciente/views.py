from django.shortcuts import render

# Create your views here.
def pacientes(request):
    return render(request, "paciente/viewPaciente.html")

def pacienteDetalles(request):
    return render(request, "paciente/viewPacienteInfo.html")
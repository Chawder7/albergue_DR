from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count
from .models import Paciente
from receta.models import Receta
from .forms import PacienteForm
from django.contrib import messages
from utils import utils

# Create your views here.
def pacientes(request):
    query = request.GET.get('busqueda','')
    pacientes =  Paciente.objects.annotate(num_recetas=Count('receta')).only("id","nombrePaciente","apellidoPaciente","edad","genero")

    if query:
        pacientes = pacientes.filter(
            Q(nombrePaciente__icontains=query) | 
            Q(apellidoPaciente__icontains=query)
        )

    paginacion = utils.paginar(pacientes, request)

    return render(request, "paciente/viewPaciente.html",{'pacientes':paginacion, 'query':query})

def pacienteDetalles(request, id):
    paciente = Paciente.objects.get(id=id)
    recetas = Receta.objects.filter(paciente_id=id)
    return render(request, "paciente/viewPacienteInfo.html", {'paciente':paciente, 'recetas':recetas})

def registrarPaciente(request):
    if request.method == 'POST':
        formPac = PacienteForm(request.POST, request.FILES)
        if formPac.is_valid():
            nombrePaciente = request.POST['nombrePaciente']
            apellidoPaciente = request.POST['apellidoPaciente']
            edad = request.POST['edad']
            genero = request.POST['genero']
            fotoPaciente = request.FILES['fotoPaciente']
            insert = Paciente(nombrePaciente = nombrePaciente, apellidoPaciente = apellidoPaciente, edad = edad, genero = genero, fotoPaciente = fotoPaciente)
            insert.save()
            return redirect('Pacientes')
        else:
            messages.error(request, "Error al procesar el formulario")
    else: 
        return render(request, "paciente/formPaciente.html", {'paciente': Paciente})

def eliminarPaciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('Pacientes')

def editarPaciente(request, id):
    paciente = Paciente.objects.get(id=id)
    return render(request, "paciente/editarPaciente.html", {'paciente': paciente})

def actualizarPaciente(request, id):
    aPaciente = get_object_or_404(Paciente, id=id)
    form = PacienteForm(request.POST, request.FILES, instance = aPaciente)
    if form.is_valid():
        form.save()
        return redirect('Pacientes')
    return render(request, "paciente/editarPaciente.html", {'paciente':aPaciente})

def formPaciente(request):
    return render(request, "paciente/formPaciente.html")

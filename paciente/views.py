from django.shortcuts import render
from django.db.models import Q, Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Paciente
from receta.models import Receta
from .forms import PacienteForm
from django.contrib import messages

# Create your views here.
def pacientes(request):
    query = request.GET.get('busqueda','')
    lista_pacientes =  Paciente.objects.annotate(num_recetas=Count('receta')).only("id","nombrePaciente","apellidoPaciente","edad","genero")

    if query:
        pacientes = pacientes.filter(
            Q(nombrePaciente__icontains=query) | 
            Q(apellidoPaciente__icontains=query)
        )

    paginacion = Paginator(lista_pacientes,1)
    pagina = request.GET.get('page')
    try:
        pacientes = paginacion.page(pagina)
    except PageNotAnInteger:
        pacientes = paginacion.page(1)
    except EmptyPage:
        pacientes = paginacion.page(paginacion.num_pages)

    return render(request, "paciente/viewPaciente.html",{'pacientes':pacientes, 'query':query})

def pacienteDetalles(request):
    return render(request, "paciente/viewPacienteInfo.html")

def formPaciente(request):
    return render(request, "paciente/formPaciente.html")

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
            return render(request, "paciente/formPaciente.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else: 
        return render(request, "paciente/formPaciente.html", {'paciente': Paciente})
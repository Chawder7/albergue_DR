from django.shortcuts import render, get_object_or_404
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
        lista_pacientes = lista_pacientes.filter(
            Q(nombrePaciente__icontains=query) | 
            Q(apellidoPaciente__icontains=query)
        )

    paginacion = Paginator(lista_pacientes,8)
    pagina = request.GET.get('page')
    try:
        lista_pacientes = paginacion.page(pagina)
    except PageNotAnInteger:
        lista_pacientes = paginacion.page(1)
    except EmptyPage:
        lista_pacientes = paginacion.page(paginacion.num_pages)

    return render(request, "paciente/viewPaciente.html",{'pacientes':lista_pacientes, 'query':query})

def pacienteDetalles(request, id):
    paciente = Paciente.objects.get(id=id)
    return render(request, "paciente/viewPacienteInfo.html", {'paciente':paciente})

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
            query = request.GET.get('busqueda','')
            lista_pacientes =  Paciente.objects.annotate(num_recetas=Count('receta')).only("id","nombrePaciente","apellidoPaciente","edad","genero")
            if query:
                pacientes = pacientes.filter(
                    Q(nombrePaciente__icontains=query) | 
                    Q(apellidoPaciente__icontains=query)
                )
            paginacion = Paginator(lista_pacientes,8)
            pagina = request.GET.get('page')
            try:
                pacientes = paginacion.page(pagina)
            except PageNotAnInteger:
                pacientes = paginacion.page(1)
            except EmptyPage:
                pacientes = paginacion.page(paginacion.num_pages)
            return render(request, "paciente/viewPaciente.html",{'pacientes':pacientes, 'query':query})
        else:
            messages.error(request, "Error al procesar el formulario")
    else: 
        return render(request, "paciente/formPaciente.html", {'paciente': Paciente})

def eliminarPaciente(request, id, confirmacion='paciente/confirmarEliminacion.html'):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method=='POST':
        paciente.delete()
        pacientes=Paciente.objects.all()
        return render(request, "paciente/viewPaciente.html", {'pacientes':pacientes})
    return render(request, confirmacion, {'object':paciente})

def editarPaciente(request, id):
    paciente = Paciente.objects.get(id=id)
    return render(request, "paciente/editarPaciente.html", {'paciente': paciente})

def actualizarPaciente(request, id):
    aPaciente = get_object_or_404(Paciente, id=id)
    form = PacienteForm(request.POST, request.FILES, instance = aPaciente)
    if form.is_valid():
        form.save()
        query = request.GET.get('busqueda','')
        lista_pacientes =  Paciente.objects.annotate(num_recetas=Count('receta')).only("id","nombrePaciente","apellidoPaciente","edad","genero")
        if query:
            pacientes = pacientes.filter(
                Q(nombrePaciente__icontains=query) | 
                Q(apellidoPaciente__icontains=query)
            )
        paginacion = Paginator(lista_pacientes,8)
        pagina = request.GET.get('page')
        try:
            pacientes = paginacion.page(pagina)
        except PageNotAnInteger:
            pacientes = paginacion.page(1)
        except EmptyPage:
            pacientes = paginacion.page(paginacion.num_pages)
        return render(request, "paciente/viewPaciente.html",{'pacientes':pacientes, 'query':query})
    return render(request, "paciente/editarPaciente.html", {'paciente':aPaciente})

def formPaciente(request):
    return render(request, "paciente/formPaciente.html")

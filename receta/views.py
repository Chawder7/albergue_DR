from django.shortcuts import render
from .models import Paciente
from .models import Medicamentos
from django.contrib.auth.models import User
from django.db.models import Q
from receta.models import Receta
from .forms import RecetaForm
from django.shortcuts import get_object_or_404, redirect
from utils import utils 


# Create your views here.

def viewReceta(request):
    query = request.GET.get('busqueda','')
    recetas = Receta.objects.all()

    if query:
        recetas = recetas.filter(
            Q(paciente__nombrePaciente__icontains=query) | 
            Q(doctor__username__icontains=query)
        )
    paginacion = utils.paginar(recetas, request)
    return render(request,"receta/viewRecetas.html",{'recetas':paginacion, 'query':query})

def recetaDetalles(request, id):
    receta = Receta.objects.get(id=id)
    return render(request, "receta/viewRecetasInfo.html", {'receta': receta})

def eliminarReceta(id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    return redirect('Recetas')  

def registrarReceta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            receta = form.save(commit=False)
            medicamento = get_object_or_404(Medicamentos, id = receta.medicamento.id)        
            if receta.cantidad <= medicamento.cantidad:
                medicamento.cantidad -= receta.cantidad
                medicamento.save()
                receta.save()
                return redirect('Recetas')
        else:
            error = "No hay suficiente cantidad del medicamento disponible"
            return render(request, 'receta/recetaForm.html', {'form': form, 'error':error})
    else:
        form = RecetaForm()
    pacientes = Paciente.objects.all()
    medicamentos = Medicamentos.objects.all()
    usuarios = User.objects.all()
    return render(request, 'receta/recetaForm.html', {'form': form, 'pacientes': pacientes, 'medicamentos': medicamentos, 'usuarios': usuarios})
    
def editarReceta(request, id):
    receta = Receta.objects.get(id=id)
    pacientes = Paciente.objects.all()
    medicamentos = Medicamentos.objects.all()
    usuarios = User.objects.all()
    return render(request, "receta/editarReceta.html",{'receta':receta, 'pacientes': pacientes, 'medicamentos': medicamentos, 'usuarios': usuarios})

def actualizarReceta(request, id):
    aReceta = get_object_or_404(Receta, id=id)
    form = RecetaForm(request.POST, request.FILES, instance = aReceta)
    if form.is_valid():
        form.save()
        return redirect('Recetas')
    return render(request, "paciente/editarPaciente.html", {'receta':aReceta})
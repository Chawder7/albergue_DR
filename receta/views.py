from django.shortcuts import render
from .models import Paciente
from .models import Medicamentos
from django.contrib.auth.models import User
from django.db.models import Q
from receta.models import Receta
from .forms import RecetaForm
from django.shortcuts import get_object_or_404, redirect
from utils import utils 
from django.contrib.auth.decorators import login_required


import logging


# Create your views here.

@login_required
def viewReceta(request):
    isAdmin = utils.checkRol(request)

    query = request.GET.get('busqueda','')
    recetas = Receta.objects.all()

    if query:
        recetas = recetas.filter(
            Q(paciente__nombrePaciente__icontains=query) | 
            Q(doctor__username__icontains=query) |
            Q(id__icontains=query)
        )
    paginacion = utils.paginar(recetas, request)
    return render(request,"receta/viewRecetas.html",{'recetas':paginacion, 'query':query, 'isAdmin':isAdmin})

@login_required
def recetaDetalles(request, id):
    receta = Receta.objects.get(id=id)
    return render(request, "receta/viewRecetasInfo.html", {'receta': receta})

@login_required
def eliminarReceta(id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    return redirect('Recetas')  

@login_required
def registrarReceta(request):
    pacientes = Paciente.objects.all()
    medicamentos = Medicamentos.objects.all()
    usuarios = User.objects.all()
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
                print(error)
                return render(request, 'receta/recetaForm.html', {'form': form,'error':error, 'pacientes': pacientes, 'medicamentos': medicamentos, 'usuarios': usuarios})
    else:
        form = RecetaForm()
    return render(request, 'receta/recetaForm.html', {'form': form, 'pacientes': pacientes, 'medicamentos': medicamentos, 'usuarios': usuarios})
    
@login_required
def editarReceta(request, id):
    receta = Receta.objects.get(id=id)
    pacientes = Paciente.objects.all()
    medicamentos = Medicamentos.objects.all()
    usuarios = User.objects.all()
    return render(request, "receta/editarReceta.html",{'receta':receta, 'pacientes': pacientes, 'medicamentos': medicamentos, 'usuarios': usuarios})

@login_required
def actualizarReceta(request, id):
    receta = get_object_or_404(Receta, id=id)
    form = RecetaForm(request.POST, request.FILES, instance = receta)
    if form.is_valid():
        medicamento = get_object_or_404(Medicamentos, id = receta.medicamento.id)
        if receta.cantidad <= medicamento.cantidad:
            medicamento.cantidad -= receta.cantidad
            medicamento.save()
            receta.save()
            return redirect('Recetas')
        else:
            error = "No hay suficiente cantidad del medicamento disponible"
            print(error)
            return redirect('Recetas')
    return render(request, "paciente/editarPaciente.html", {'receta':receta})
from django.shortcuts import render
from .models import Paciente
from .models import Medicamentos
from django.contrib.auth.models import User
from receta.models import Receta
from .forms import RecetaForm

# Create your views here.

def viewReceta(request):
    recetas = Receta.objects.all()
    return render(request,"receta/viewRecetas.html", {'recetas': recetas})

def recetaDetalles(request, id):
    receta = Receta.objects.get(id=id)
    return render(request, "receta/viewRecetasInfo.html", {'receta': receta})

def registrarReceta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'receta/recetaForm.html')
    else:
        form = RecetaForm()

    pacientes = Paciente.objects.all()
    medicamentos = Medicamentos.objects.all()
    usuarios = User.objects.all()
    return render(request, 'receta/recetaForm.html', {'form': form, 'pacientes': pacientes, 'medicamentos': medicamentos, 'usuarios': usuarios})


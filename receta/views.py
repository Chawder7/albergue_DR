from django.shortcuts import render
from .models import Paciente
from .models import Medicamentos
from django.contrib.auth.models import User
from receta.models import Receta
from .forms import RecetaForm

# Create your views here.

def viewReceta(request):
    return render(request,"receta/viewRecetas.html")

def recetaDetalles(request):
    return render(request, "receta/viewRecetasInfo.html")

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


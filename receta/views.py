from django.shortcuts import render
from .models import Paciente
from .models import Medicamentos
from receta.models import Receta

# Create your views here.

def viewReceta(request):
    return render(request,"receta/viewRecetas.html")

def recetaDetalles(request):
    return render(request, "receta/viewRecetasInfo.html")

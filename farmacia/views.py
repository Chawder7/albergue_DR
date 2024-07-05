from django.shortcuts import render
from .forms import MedicamentoForm
from .models import Medicamentos
from django.contrib import messages

# Create your views here.
def altaMedicamento(request):
    return render(request, "farmacia/farmacia.html")

def registrarMedicamento(request):
    if request.method == 'POST':
        formMed = MedicamentoForm(request.POST, request.FILES)
        if formMed.is_valid():
            nombreMed = request.POST['nombreMed']
            categoria = request.POST['categoria']
            cantidad = request.POST['cantidad']
            fechaVen = request.POST['fechaVen']
            descripcion = request.POST['descripcion']
            fotoMed = request.FILES['fotoMed']
            insert = Medicamentos(nombreMed = nombreMed, categoria = categoria, cantidad = cantidad, fechaVen = fechaVen, descripcion = descripcion, fotoMed = fotoMed)
            insert.save()
            return render(request, "farmacia/farmacia.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else: 
        return render(request, "farmacia/farmacia.html", {'medicamento': Medicamentos})

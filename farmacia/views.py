from django.shortcuts import render, get_object_or_404, redirect
from .forms import MedicamentoForm
from .models import Medicamentos
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
# Crear la vista para agregar un medicamento
def altaMedicamento(request):
    return render(request, "farmacia/formFarmacia.html")

# Crear la vista para registrar un medicamento
def registrarMedicamento(request):
    if request.method == 'POST':
        formMed = MedicamentoForm(request.POST, request.FILES)
        if formMed.is_valid():
            formMed.save()
            return redirect('Medicamentos')
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        formMed = MedicamentoForm()
        
    return render(request, "farmacia/formFarmacia.html", {'form': formMed})

# Crear la vista para listar todos los medicamentos
def allMedicamentos(request):
    medicamentos = Medicamentos.objects.all().only("id", "nombreMed", "descripcion", "categoria", "cantidad", "fechaVen")
    lowMeds = Medicamentos.objects.filter(cantidad__lte=20)
    consulta = {
        "medicamentos": medicamentos,
        "lowMeds": lowMeds
    }
    return render(request, "farmacia/viewFarmacia.html", consulta)

def altaMedicamento(request):
    return render(request, "farmacia/formFarmacia.html")

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
            return render(request, "farmacia/formFarmacia.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else: 
        return render(request, "farmacia/formFarmacia.html", {'medicamento': Medicamentos})

def consultarMedicamentoIndividual(request, id):
    medicamento = get_object_or_404(Medicamentos, id=id)
    form = MedicamentoForm(instance=medicamento)
    return render(request, "farmacia/formFarmacia.html", {"form": form, "medicamento": medicamento})

def editarMedicamento(request, id):
    medicamento = get_object_or_404(Medicamentos, id=id)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, request.FILES)
        if form.is_valid():
            nombreMed = request.POST['nombreMed']
            categoria = request.POST['categoria']
            cantidad = request.POST['cantidad']
            fechaVen = request.POST['fechaVen']
            descripcion = request.POST['descripcion']
            fotoMed = request.FILES['fotoMed']

            medicamento.nombreMed = nombreMed
            medicamento.categoria = categoria
            medicamento.cantidad = cantidad
            medicamento.fechaVen = fechaVen
            medicamento.descripcion = descripcion
            medicamento.fotoMed = fotoMed
            medicamento.save()
            return redirect('Medicamentos')
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request, "farmacia/formFarmacia.html", {"medicamento": medicamento})

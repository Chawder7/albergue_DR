from django.shortcuts import render, get_object_or_404, redirect
from .forms import MedicamentoForm
from .models import Medicamentos
from django.contrib import messages


# Crear la vista para listar todos los medicamentos
def allMedicamentos(request):
    medicamentos = Medicamentos.objects.all().only("id", "nombreMed", "descripcion", "categoria", "cantidad", "fechaVen")
    lowMeds = Medicamentos.objects.filter(cantidad__lte=20)
    consulta = {
        "medicamentos": medicamentos,
        "lowMeds": lowMeds
    }
    return render(request, "farmacia/viewFarmacia.html", consulta)


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
    return render(request, "farmacia/formFarmacia.html", {'form': formMed})


# Crear la vista para consultar un medicamento individual
def consultarMedicamentoIndividual(request, id):
    medicamento = get_object_or_404(Medicamentos, id=id)
    form = MedicamentoForm(instance=medicamento)
    return render(request, "farmacia/formFarmacia.html", {"form": form, "medicamento": medicamento})

# Crear la vista para editar un medicamento
def editarMedicamento(request, id):
    medicamento = get_object_or_404(Medicamentos, id=id)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, request.FILES, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('Medicamentos')
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, "farmacia/formFarmacia.html", {"form": form, "medicamento": medicamento})

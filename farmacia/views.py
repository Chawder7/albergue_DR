from django.shortcuts import render, get_object_or_404, redirect
from .forms import MedicamentoForm
from .models import Medicamentos
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from utils import utils

@login_required
def allMedicamentos(request):
    isAdmin = utils.checkRol(request)
    
    query = request.GET.get('busqueda','')
    medicamentos = Medicamentos.objects.all().only("id", "nombreMed", "descripcion", "categoria", "cantidad", "fechaVen")
    lowMeds = Medicamentos.objects.filter(cantidad__lte=10)
    consulta = {
        "lowMeds": lowMeds
    }
    if query:
        medicamentos = medicamentos.filter(
            Q(nombreMed__icontains=query ) 
        )
    paginacion = utils.paginar(medicamentos, request, items_per_page=5)
    
    return render(request, "farmacia/viewFarmacia.html", {'consulta':consulta, 'query':query, 'medicamentos':paginacion, 'isAdmin':isAdmin})

@login_required
def altaMedicamento(request):
    return render(request, "farmacia/formFarmacia.html")

@login_required
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
            messages.success(request, "Medicamento registrado con éxito")
            return redirect('Medicamentos')
        else:
            messages.error(request, "Error al procesar el formulario")
    else: 
        return render(request, "farmacia/formFarmacia.html", {'medicamento': Medicamentos})

@login_required
def consultarMedicamentoIndividual(request, id):
    medicamento = get_object_or_404(Medicamentos, id=id)
    form = MedicamentoForm(instance=medicamento)
    return render(request, "farmacia/formFarmacia.html", {"form": form, "medicamento": medicamento})

@login_required
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

            if 'fotoMed' in request.FILES:
                medicamento.fotoMed = request.FILES['fotoMed']
            else:
                medicamento.fotoMed = medicamento.fotoMed
            medicamento.nombreMed = nombreMed
            medicamento.categoria = categoria
            medicamento.cantidad = cantidad
            medicamento.fechaVen = fechaVen
            medicamento.descripcion = descripcion

            medicamento.save()
            return redirect('Medicamentos')
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        form = MedicamentoForm(instance=medicamento)
    return render(request, "farmacia/formFarmacia.html", {"form": form, "medicamento": medicamento})

@login_required
def eliminarMed(request, id):
    medicamento = get_object_or_404(Medicamentos, id=id)
    medicamento.delete()
    return redirect('Medicamentos')

from django.shortcuts import render
from .models import Paciente
from .models import Medicamentos
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from receta.models import Receta
from .forms import RecetaForm
from django.shortcuts import get_object_or_404


# Create your views here.

def viewReceta(request):
    query = request.GET.get('busqueda','')
    recetas = Receta.objects.all()

    if query:
        recetas = recetas.filter(
            Q(paciente__nombrePaciente__icontains=query) | 
            Q(doctor__username__icontains=query)
        )

    paginacion = Paginator(recetas,8)
    pagina = request.GET.get('page')
    try:
        recetas = paginacion.page(pagina)
    except PageNotAnInteger:
        recetas = paginacion.page(1)
    except EmptyPage:
        recetas = paginacion.page(paginacion.num_pages)

    return render(request,"receta/viewRecetas.html",{'recetas':recetas, 'query':query})

def recetaDetalles(request, id):
    receta = Receta.objects.get(id=id)
    return render(request, "receta/viewRecetasInfo.html", {'receta': receta})

def eliminarReceta(request, id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    recetas = Receta.objects.all()
    return render(request, 'receta/viewRecetas.html', {'recetas': recetas})   

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
                return render(request, 'receta/recetaForm.html')
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
        recetas = Receta.objects.all()
        return render(request,"receta/viewRecetas.html",{'recetas':recetas})
    return render(request, "paciente/editarPaciente.html", {'receta':aReceta})
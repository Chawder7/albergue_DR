from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from receta.models import Receta

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

def recetaDetalles(request):
    return render(request, "receta/viewRecetasInfo.html")
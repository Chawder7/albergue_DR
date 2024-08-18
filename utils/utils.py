from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginar(queryset, request, items_per_page=8):
    paginacion = Paginator(queryset, items_per_page)
    pagina = request.GET.get('page')
    try:
        objetos_paginados = paginacion.page(pagina)
    except PageNotAnInteger:
        objetos_paginados = paginacion.page(1)
    except EmptyPage:
        objetos_paginados = paginacion.page(paginacion.num_pages)
    
    return objetos_paginados
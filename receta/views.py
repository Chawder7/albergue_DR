from django.shortcuts import render

# Create your views here.

def viewReceta(request):
    return render(request,"receta/viewRecetas.html")
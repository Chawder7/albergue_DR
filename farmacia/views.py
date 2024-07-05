from django.shortcuts import render
from .forms import MedicamentoForm

# Create your views here.
def altaMedicamento(request):
    return render(request, "farmacia/farmacia.html")

def registrarMedicamento(request):
    if request.method == 'POST':
        formMed = MedicamentoForm(request.POST)
        if formMed.is_valid():
            formMed.save()
            print("Se guardó")
            return render(request, 'farmacia/farmacia.html')
    formMed = MedicamentoForm()
    print("Nose guardó nada")
    return render(request, 'farmacia/farmacia.html', {'formMed': formMed})
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    usuario = User.objects.all()
    return render(request, 'home/index.html', {'usuario': usuario})
"""
URL configuration for albergue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as home_views 
from farmacia import views as farmacia_views
from paciente import views as paciente_views
from django.conf import settings
from receta import views as receta_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.index, name='Index'),
    path('farmacia/', farmacia_views.allMedicamentos, name="Medicamentos"),
    path('altamedicamento/', farmacia_views.altaMedicamento, name = "AltaMed"),
    path('registrar/', farmacia_views.registrarMedicamento, name = "RegistrarMed"),
    path('pacientes/', paciente_views.pacientes, name = "Pacientes"),
    path('recetas/',receta_views.viewReceta,name="Recetas"),
    path('recetaInfo/',receta_views.recetaDetalles,name="infoReceta"),
    path('pacienteInfo/',paciente_views.pacienteDetalles,name="infoPaciente"),
    path('altapaciente/', paciente_views.formPaciente, name = "AltaPac"),
    path('registrarpaciente/', paciente_views.registrarPaciente, name = "RegistrarPac"),
    path('registroreceta/', receta_views.registrarReceta, name = "RegistrarReceta"),
]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,
                document_root = settings.MEDIA_ROOT)

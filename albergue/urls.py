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
    path('altamedicamento/', farmacia_views.altaMedicamento, name="AltaMed"),
    path('registrar/', farmacia_views.registrarMedicamento, name="RegistrarMed"),
    path('editarMedicamento/<int:id>/', farmacia_views.editarMedicamento, name="ActualizarMed"),  # Corregido
    path('consultarMedicamento/<int:id>/', farmacia_views.consultarMedicamentoIndividual, name="GetMedicamento"),
    

    path('pacientes/', paciente_views.pacientes, name="Pacientes"),
    path('pacienteInfo/',paciente_views.pacienteDetalles,name="infoPaciente"),
    path('registrarpaciente/', paciente_views.registrarPaciente, name="RegistrarPac"),
    path('altapaciente/', paciente_views.formPaciente, name="AltaPac"),

    path('recetas/',receta_views.viewReceta,name="Recetas"),
    path('recetaInfo/',receta_views.recetaDetalles,name="infoReceta"),
    path('registroreceta/', receta_views.registrarReceta, name="RegistrarReceta"),
]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,
                document_root=settings.MEDIA_ROOT)

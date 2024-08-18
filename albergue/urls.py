from django.contrib import admin
from django.urls import path
from home import views as home_views 
from farmacia import views as farmacia_views
from paciente import views as paciente_views
from django.conf import settings
from receta import views as receta_views

urlpatterns = [
    #ADMIN
    path('admin/', admin.site.urls),

    #HOME
    path('', home_views.index, name='Index'),

    #FARMACIA
    path('farmacia/', farmacia_views.allMedicamentos, name="Medicamentos"),
    path('altamedicamento/', farmacia_views.altaMedicamento, name = "AltaMed"),
    path('registrar/', farmacia_views.registrarMedicamento, name = "RegistrarMed"),
    path('editarMedicamento/<int:id>/', farmacia_views.editarMedicamento, name="ActualizarMed"),
    path('consultarMedicamento/<int:id>/', farmacia_views.consultarMedicamentoIndividual, name="GetMedicamento"),
    path('eliminarmed/<int:id>/',farmacia_views.eliminarMed,name="EliminarMed"),

    #RECETAS
    path('recetas/', receta_views.viewReceta, name="Recetas"),
    path('registroreceta/', receta_views.registrarReceta, name = "RegistrarReceta"),
    path('recetaInfo/<int:id>/', receta_views.recetaDetalles, name="infoReceta"),
    path('eliminarReceta/<int:id>/', receta_views.eliminarReceta, name="DeleteReceta"),
    
    #PACIENTES
    path('pacienteInfo/<int:id>', paciente_views.pacienteDetalles, name="infoPaciente"),
    path('pacientes/', paciente_views.pacientes, name="Pacientes"),
    path('registrarpaciente/', paciente_views.registrarPaciente, name="RegistrarPac"),
    path('editarPaciente/<int:id>', paciente_views.editarPaciente, name="Editar"), 
    path('actualizarPaciente/<int:id>', paciente_views.actualizarPaciente, name="Actualizar"),
    path('eliminarPaciente/<int:id>', paciente_views.eliminarPaciente, name="Eliminar"),
    path('altapaciente/', paciente_views.formPaciente, name="AltaPac"),


]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,
                document_root=settings.MEDIA_ROOT)

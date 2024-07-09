from django.db import models
from paciente.models import Paciente
from django.contrib.auth.models import User
from  farmacia.models import Medicamentos
from ckeditor.fields import RichTextField

# Create your models here.

class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Doctor")
    diagnostico = RichTextField(verbose_name="Diagnostico")
    medicamento = models.ForeignKey(Medicamentos, on_delete=models.CASCADE, verbose_name="Medicamento")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
        ordering = ["-created"]
    
    def __int__(self):
        return self.id
from django.db import models

# Create your models here.

genero_opcion = [
    (1, 'M'),
    (2, 'F'),
    
]


class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nombrePaciente = models.TextField(verbose_name="Nombre")
    apellidoPaciente = models.TextField(verbose_name="Apellido", null=True, blank=True)
    edad = models.IntegerField(verbose_name="Edad")
    genero = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Genero",
        choices = genero_opcion,
        default=1)
    fotoPaciente = models.ImageField(upload_to="fotoPaciente", blank=True, null=True, verbose_name="Fotografia")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ["-id"]
    
    def __str__(self):
        return self.nombrePaciente

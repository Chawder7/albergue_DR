from django.db import models

# Tabla de medicamentos

class Medicamentos(models.Model):
    id = models.AutoField(primary_key = True)
    nombreMed = models.TextField(verbose_name = "Nombre de medicamento", null = True)
    categoria = models.TextField(verbose_name = "Categoría", null = True)
    cantidad = models.IntegerField(verbose_name = "Cantidad", null = True)
    fechaVen = models.DateField(verbose_name = "Fecha de vencimiento", null = True)
    descripcion = models.TextField(verbose_name = "Descripción del medicamento", null = True)
    fotoMed = models.FileField(upload_to = "fotosMedicamentos", blank = True, null = True, verbose_name = "Foto del medicamento")
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
        ordering = ["cantidad"]

    def __str__(self):
        return self.nombreMed
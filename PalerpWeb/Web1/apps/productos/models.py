from django.db import models

# Create your models here.

class Producto(models.Model):
    codigo = models.CharField(max_length = 30, default = "")
    minicodigo = models.CharField(max_length = 10, default = "")
    codigofabricante = models.CharField(max_length = 30, default = "")
    nombre = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 300)
    categoria = models.CharField(max_length = 100)
    precio = models.FloatField(default = 9.99)
    cadenacaracteristicas = models.TextField(default = "")

    def __str__(self):
        return self.nombre

# mi_app/models.py

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()

    def __str__(self):
        return self.nombre


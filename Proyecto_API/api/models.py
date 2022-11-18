from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=100)
    cedula=models.CharField(max_length=10)
    telefono=models.CharField(max_length=10)
    correo=models.CharField(max_length=50)
    clave=models.CharField(max_length=200)
    numCuenta=models.PositiveIntegerField()
    saldo=models.PositiveIntegerField()
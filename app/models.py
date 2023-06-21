from django.db import models

# Create your models here.
class registro(models.Model):
    rut              = models.CharField(max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)

class Pan(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)
    valor = models.IntegerField(max_length=20)

class biografia (models.Model):
    descripcion = models.TextField(max_length=100)


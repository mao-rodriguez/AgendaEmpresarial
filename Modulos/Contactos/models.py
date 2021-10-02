from django.db import models
from django.db.models.base import Model

# Create your models here.

class Empresa(models.Model):
    #Id = models.CharField (max_length=10, primary_key=True)
    NIT = models.CharField(max_length=11)
    Nombre = models.CharField(max_length=50)
    Telefono =  models.CharField(max_length=10)
    Direccion =  models.CharField(max_length= 100)
    Ciudad =  models.CharField(max_length= 50)
        
    def empresa(self):
        txt = "{0}"
        return txt.format(self.Nombre)

class Contacto(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Compañia =  models.ForeignKey(Empresa, null=False, blank=False, on_delete=models.CASCADE)
    Cargo =  models.CharField(max_length=20)
    Email =  models.CharField(max_length=50)
    Celular =  models.CharField(max_length=10)
    Direccion =  models.CharField(max_length=100)
    Ciudad =  models.CharField(max_length=50)
    Estado = models.BooleanField(default=True)
    
    def nombreCompleto(self):
        txt = "{0}, {1}"
        return txt.format(self.Apellido, self.Nombre)

    def __str__(self):
        txt = "{0} de la Empresa {1} se encuentra: {2}"
        if self.Estado:
            estadoContacto = "Activo"
        else:
            estadoContacto = "Inactivo"
        return txt.format(self.nombreCompleto, self.Empresa, estadoContacto)
from django.db import models
 
class Localidad(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Pista(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    estado = models.CharField(max_length = 50)
    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    costo = models.FloatField(max_length=50)
    horario = models.TimeField(max_length=50)
    capacidad = models.IntegerField(max_length=50)
    reserva = models.BooleanField(max_length=50)
    def __str__(self):
        return self.nombre

class Estacion(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    superficie = models.FloatField(max_length=50)
    pista = models.ManyToManyField(Pista)
    precio_dia = models.FloatField(max_length=50)
    horario = models.TimeField(max_length=50)
    telefono = models.IntegerField(max_length=50)
    estado = models.CharField(max_length = 50)
    servicio = models.ManyToManyField(Servicio)
    def __str__(self):
        return self.nombre

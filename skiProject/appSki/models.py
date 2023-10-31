from django.db import models
 
class Localidad(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    latitud = models.FloatField
    longitud = models.FloatField

class Pista(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    longitud = models.FloatField
    estado = models.CharField(max_length = 50)

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    costo = models.FloatField
    horario = models.TimeField
    capacidad = models.IntegerField
    reserva = models.BooleanField

class Estacion(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    pista = models.ManyToManyField(Pista)
    precio_dia = models.FloatField
    horario = models.TimeField
    telefono = models.IntegerField()
    estado = models.CharField(max_length = 50)
    servicio = models.ManyToManyField(Servicio)

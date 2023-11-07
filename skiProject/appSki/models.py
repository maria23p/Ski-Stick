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
    costo = models.FloatField(default=0.0)
    horario = models.TimeField(default='00:00:00')
    capacidad = models.IntegerField(default=0)
    reserva = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre

class Estacion(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    superficie = models.FloatField(default=0.0)
    precio_dia = models.FloatField(default=0.0)
    horario = models.TimeField(default='00:00:00')
    telefono = models.IntegerField(default=0)
    estado = models.CharField(max_length = 50)
    pistas = models.ManyToManyField(Pista, through='EstacionPista')
    servicios = models.ManyToManyField(Servicio, through='EstacionServicio')
    #servicio = models.ManyToManyField(Servicio)
    def __str__(self):
        return self.nombre

class EstacionPista(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    pista = models.ForeignKey(Pista, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.estacion.nombre} - {self.pista.nombre}'

class EstacionServicio(models.Model):
    estacion = models.ForeignKey(Estacion, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.estacion.nombre} - {self.servicio.nombre}'
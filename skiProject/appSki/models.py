from django.db import models
# para la traduccion por ejemplo de los servicios
from django.utils.translation import gettext_lazy as _

class Localidad(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
    def __str__(self):
        return self.nombre

class Pista(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    color = models.CharField('Color', max_length=50)
    estado = models.CharField('Estado',max_length = 50)
    
    def __str__(self):
        return self.nombre
   #  def color_en_idioma(self, idioma):
    #    if idioma == 'es':
     #       return _(self.color)  # Traducción al español
     #   elif idioma == 'en':
            # Traducción al inglés
    #        if self.color.lower() == 'roja':
     #           return 'red'
            # Agrega más traducciones según sea necesario para otros colores en inglés
      #      else:
       #         return self.color
        #else:
         #   return self.color  """
       
    
   

class Servicio(models.Model):
    nombre = models.CharField(_('Nombre'), max_length=50)
    def __str__(self):
        return self.nombre

class Estacion(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    superficie = models.FloatField(default=0.0)
    precio_dia = models.FloatField(default=0.0)
    horario_ini = models.TimeField(default='00:00:00')
    horario_fin = models.TimeField(default='00:00:00')
    telefono = models.IntegerField(default=0)
    estado = models.CharField(max_length = 50)
    pistas = models.ManyToManyField(Pista, through='EstacionPista')
    servicios = models.ManyToManyField(Servicio, through='EstacionServicio')
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')

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
    costo = models.FloatField(default=0.0)
    reserva = models.BooleanField(default=False)
    horario_ini = models.TimeField(default='00:00:00')
    horario_fin = models.TimeField(default='00:00:00')
    
    def __str__(self):
        return f'{self.estacion.nombre} - {self.servicio.nombre}'
    
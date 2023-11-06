from django.contrib import admin
from django.contrib import admin
from .models import Localidad, Pista, Servicio, Estacion, EstacionPista,EstacionServicio

# Register your models here.

admin.site.register(Localidad)
admin.site.register(Pista)
admin.site.register(Servicio)
admin.site.register(Estacion)
admin.site.register(EstacionPista)
admin.site.register(EstacionServicio)

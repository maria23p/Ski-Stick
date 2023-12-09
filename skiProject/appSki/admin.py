from django.contrib import admin
from .models import Localidad, Pista, Servicio, Estacion, EstacionPista,EstacionServicio, ViajesEnGrupo

# Register your models here.

admin.site.register(Localidad)
admin.site.register(Pista)
admin.site.register(Servicio)
admin.site.register(Estacion)
admin.site.register(EstacionPista)
admin.site.register(EstacionServicio)
admin.site.register(ViajesEnGrupo)

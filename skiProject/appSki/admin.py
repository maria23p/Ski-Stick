from django.contrib import admin
from django.contrib import admin
from .models import Localidad, Pista, Servicio, Estacion

# Register your models here.

admin.site.register(Localidad)
admin.site.register(Pista)
admin.site.register(Servicio)
admin.site.register(Estacion)


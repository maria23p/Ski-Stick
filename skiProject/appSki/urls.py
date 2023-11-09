from django.urls import path
from . import views

urlpatterns = [
path('', views.index_localidades, name='index'),
path('localidades/<int:localidad_id>/estaciones', views.index_estaciones, name='estaciones'),
path('estaciones/<int:estacion_id>', views.show_estacion, name='estacion'),
path('pistas/<int:pista_id>', views.show_pista, name='pista'),
path('servicios/<int:servicio_id>', views.show_servicio, name='servicio'),

]
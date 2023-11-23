from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('localidades/', views.index_localidades, name='localidades'),
path('todas_estaciones/', views.estaciones_todas, name = 'estaciones_todas'),
path('todas_pistas/', views.pistas_todas, name='pistas_todas'),
path('todos_servicios/', views.servicios_todos, name='servicios_todos'),
path('localidades/<int:localidad_id>/estaciones', views.index_estaciones, name='estaciones'),
path('estaciones/<int:estacion_id>', views.show_estacion, name='estacion'),
path('pistas/<int:pista_id>', views.show_pista, name='pista'),
path('servicios/<int:servicio_id>', views.show_servicio, name='servicio'),
path('show_formulario/', views.show_formulario, name='show_formulario'),
]

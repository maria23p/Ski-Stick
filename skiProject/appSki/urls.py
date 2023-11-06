from django.urls import path
from . import views

urlpatterns = [
 path('', views.index_localidades, name='index'),
 path('localidades/<int:localidad_id>/', views.show_localidad, name='detail'),
 path('localidades/<int:localidad_id>/estaciones', views.index_estaciones, name='estaciones'),
]
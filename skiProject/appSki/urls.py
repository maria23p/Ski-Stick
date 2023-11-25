from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _



urlpatterns = [
path('', views.PortadaListView.as_view(), name='index'),
path('localidades/', views.LocalidadesListView.as_view(), name='localidades'),
path('todas_estaciones/', views.EstacionesListView.as_view(), name = 'estaciones_todas'),
path('todas_pistas/', views.PistasListView.as_view(), name='pistas_todas'),
path('todos_servicios/', views.ServiciosListView.as_view(), name='servicios_todos'),
path('localidades/<int:pk>/estaciones', views.EstacionesLocalidadListView.as_view(), name='estaciones'),
path('estaciones/<int:pk>', views.EstacionDetailView.as_view(), name='estacion'),
path('pistas/<int:pk>', views.PistaDetailView.as_view(), name='pista'),
path('servicios/<int:pk>', views.ServicioDetailView.as_view(), name='servicio'),
path('show_formulario/', views.FormularioView.as_view(), name='show_formulario'),
path('set-language/<str:language>/', views.set_language, name='set_language'),
]

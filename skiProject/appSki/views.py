from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Localidad, Estacion, Pista, Servicio

# Create your views here.
def index(request):
    #return HttpResponse("Listado de Localidades:")
	return render(request, 'index.html')

#devuelve el listado de localidades
def index_localidades(request):
	localidades = get_list_or_404(Localidad.objects.order_by('nombre'))
	context = {'lista_localidades': localidades }	
	return render(request, 'index.html', context)

#devuelve los datos de una localidad
def show_localidad(request, localidad_id):
	localidad = get_object_or_404(Localidad, pk=localidad_id)
	context = {'localidad': localidad }
	return render(request, 'detail.html', context)

#devuelve las estaciones de cada localidad
def index_estaciones(request, localidad_id):
	localidad = get_object_or_404(Localidad, pk=localidad_id)
	estaciones =  localidad.estacion_set.all()
	context = {'localidad': localidad, 'estaciones' : estaciones }
	return render(request, 'estaciones.html', context)

#devuelve los datos de una estacion
def show_estacion(request, estacion_id):
	estacion = get_object_or_404(Estacion, pk=estacion_id)
	pistas =  estacion.pistas.all()
	servicios = estacion.servicios.all()
	context = { 'estacion': estacion, 'pistas' : pistas, 'servicios' : servicios }
	return render(request, 'estacion.html', context)


#devuelve los detalles de una pista
def show_pista(request, pista_id):
	pista = get_object_or_404(Pista, pk=pista_id)
	estaciones =  pista.estacion_set.all()
	context = { 'estaciones': estaciones, 'pista' : pista }
	return render(request, 'pista.html', context)

#devuelve los detalles de un servicio
def show_servicio(request, servicio_id):
	servicio = get_object_or_404( Servicio, pk=servicio_id)
	estaciones =  Servicio.estacion_set.all()
	context = { 'estaciones': estaciones, 'servicio' : servicio }
	return render(request, 'servicio.html', context)


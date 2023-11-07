from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Localidad, Estacion, Pista, Servicio

# Create your views here.
def index(request):
    return HttpResponse("Listado de Localidades:")


#devuelve el listado de localidades
def index_localidades(request):
	localidades = get_list_or_404(Localidad.objects.order_by('nombre'))
	context = {'lista_localidades': localidades }	
	return render(request, 'index.html', context)

#devuelve los datos de una localidad
def show_localidad(request, localidad_id):
	localidad = get_object_or_404(Localidad, pk=localidad_id)
	output = f'Detalles de la localidad: {localidad.id}, {localidad.nombre}'
	return HttpResponse(output)

#devuelve las estaciones de cada localidad
def index_estaciones(request, localidad_id):
	localidad = get_object_or_404(Localidad, pk=localidad_id)
	output = ', '.join([e.nombre for e in localidad.estacion_set.all()])
	return HttpResponse(output)

#devuelve los datos de una estacion
def show_estacion(request, estacion_id):
	estacion = get_object_or_404(Estacion, pk=estacion_id)
	output = f'Detalles de la estacion: {estacion.id}, {estacion.nombre}, {estacion.superficie}, {estacion.precio_dia}, {estacion.horario}, {estacion.telefono}, {estacion.estado}. Pistas: {[p.nombre for p in estacion.pistas.all()]}. Servicios: {[s.nombre for s in estacion.servicios.all()]}'
	return HttpResponse(output)

#devuelve los detalles de una pista
def show_pista(request, pista_id):
	pista = get_object_or_404(Pista, pk=pista_id)
	output = f'Detalles de la pista: {pista.id}, {pista.nombre}, {pista.color}, {pista.estado}'
	return HttpResponse(output)

#devuelve los detalles de un servicio
def show_servicio(request, servicio_id):
	servicio = get_object_or_404(Servicio, pk=servicio_id)
	output = f'Detalles del servicio: {servicio.id}, {servicio.nombre}, {servicio.costo}, {servicio.horario}, {servicio.capacidad}, {servicio.reserva}'
	return HttpResponse(output)


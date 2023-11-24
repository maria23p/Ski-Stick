from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from .models import Localidad, Estacion, Pista, Servicio, EstacionServicio
from .forms import MiFormulario  

# Create your views here.
def index(request):
    #return HttpResponse("Listado de Localidades:")
    estacionesFiltradas = Estacion.objects.raw('SELECT * FROM( SELECT * FROM appSki_Estacion ORDER BY Superficie DESC) GROUP BY localidad_id')
    context = {'estaciones_filtradas': estacionesFiltradas}
    return render(request, 'index.html', context)

#devuelve el listado de localidades
def index_localidades(request):
	localidades = get_list_or_404(Localidad.objects.order_by('nombre'))
	context = {'lista_localidades': localidades }	
	return render(request, 'localidades.html', context)

#devuelve listado de estaciones
def estaciones_todas(request):
    # Obtener todas las localidades
    localidades = Localidad.objects.all()

    # Crear una lista para almacenar todas las estaciones
    todas_las_estaciones = []

    # Iterar sobre todas las localidades y obtener sus estaciones
    for localidad in localidades:
        estaciones_localidad = Estacion.objects.filter(localidad=localidad)
        todas_las_estaciones.extend(estaciones_localidad)

    # Ahora tienes todas las estaciones en la lista todas_las_estaciones
    # Puedes pasar esta lista al contexto y renderizarla en tu plantilla
    context = {'todas_las_estaciones': todas_las_estaciones}
    return render(request, 'estaciones_todas.html', context)

#devuelve listado de pistas
def pistas_todas(request):
    # Obtener todas las estaciones
    estaciones = Estacion.objects.all()

    # Crear una lista para almacenar todas las pistas
    todas_las_pistas = []

    # Iterar sobre todas las estaciones y obtener sus pistas
    for estacion in estaciones:
        pistas_estacion = Pista.objects.filter(estacion=estacion)
        todas_las_pistas.extend(pistas_estacion)

    # Ahora tienes todas las pistas en la lista todas_las_pistas
    # Puedes pasar esta lista al contexto y renderizarla en tu plantilla
    context = {'todas_las_pistas': todas_las_pistas}
    return render(request, 'pistas_todas.html', context)

#devuelve listado de servicios
def servicios_todos(request):
    # Obtener todas las estaciones
    estaciones = Estacion.objects.all()

    # Crear un conjunto para almacenar los servicios sin duplicados
    servicios_unicos = set()

    # Iterar sobre las estaciones y agregar sus servicios al conjunto
    for estacion in estaciones:
        servicios_estacion = Servicio.objects.filter(estacion=estacion)
        servicios_unicos.update(servicios_estacion)

    # Puedes pasar este conjunto al contexto y renderizarlo en tu plantilla
    context = {'servicios_unicos': servicios_unicos}
    return render(request, 'servicios_todos.html', context)

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
	servicios = EstacionServicio.objects.filter(estacion = estacion)
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
	estaciones =  servicio.estacion_set.all()
	context = { 'estaciones': estaciones, 'servicio' : servicio }
	return render(request, 'servicio.html', context)

#formulario

def show_formulario(request):
    if request.method == 'POST':
        formulario = MiFormulario(request.POST)
        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data

            # Realizar acciones con estos datos, como guardarlos en la BD, enviar un correo, etc. MIRAR ESTO!
            return redirect('index')  
    else:
        formulario = MiFormulario()
    
    return render(request, 'formulario.html', {'formulario': formulario})



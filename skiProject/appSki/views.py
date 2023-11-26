from typing import Any
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from .models import Localidad, Estacion, Pista, Servicio, EstacionServicio
from .forms import MiFormulario 
from django.views.generic import DetailView, ListView, View
from django.utils import translation
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# Portada.
class PortadaListView(ListView):
    model = Estacion
    template_name = 'index.html'
    context_object_name = 'estaciones_filtradas'

    def get_queryset(self):
        raw_query = 'SELECT * FROM (SELECT * FROM appSki_Estacion ORDER BY Superficie DESC) AS ranked_stations GROUP BY localidad_id'
        queryset = Estacion.objects.raw(raw_query)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        return context
     

#devuelve el listado de localidades
class LocalidadesListView(ListView):
    model = Localidad
    template_name = 'localidades.html'
    queryset = Localidad.objects.order_by('nombre')
    context_object_name = 'lista_localidades'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        return context

#devuelve listado de estaciones
class EstacionesListView(ListView):
    model = Estacion
    template_name = 'estaciones.html'
    queryset = Estacion.objects.order_by('nombre')
    context_object_name = 'estaciones'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        return context

#devuelve listado de pistas
class PistasListView(ListView):
    model = Pista
    template_name = 'pistas_todas.html'
    queryset = Pista.objects.order_by('nombre')
    context_object_name = 'todas_las_pistas'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        return context

#devuelve listado de servicios
class ServiciosListView(ListView):
    model = Servicio
    template_name = 'servicios_todos.html'
    queryset = Servicio.objects.order_by('nombre')
    context_object_name = 'servicios_unicos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        return context

#devuelve las estaciones de cada localidad
class EstacionesLocalidadListView(ListView):
    model = Localidad
    template_name = 'estaciones.html'
    context_object_name = 'estaciones'
    
    def get_context_data(self, **kwargs):
        localidad = get_object_or_404(Localidad, pk=self.kwargs['pk'])
        estaciones =  localidad.estacion_set.all()
        #context = super(EstacionesLocalidadListView, self).get_context_data(**kwargs)
        context = super().get_context_data(**kwargs)
        context['localidad'] = localidad
        context['estaciones'] = estaciones
        #return context

        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        return context
    

#devuelve los datos de una estacion
class EstacionDetailView(DetailView):
    model = Estacion
    template_name = 'estacion.html'

    def get_context_data(self, **kwargs):
        #estacion = get_object_or_404(Estacion, pk=self.kwargs['pk'])
        #pistas =  estacion.pistas.all()
        #servicios = EstacionServicio.objects.filter(estacion = estacion)
        #context = super(EstacionDetailView, self).get_context_data(**kwargs)
        #context['pistas'] = pistas
        #context['servicios'] = servicios
        #return context
    
        context = super().get_context_data(**kwargs)
        estacion = get_object_or_404(Estacion, pk=self.kwargs['pk'])
        pistas =  estacion.pistas.all()
        servicios = EstacionServicio.objects.filter(estacion = estacion)
        
        context['pistas'] = pistas
        context['servicios'] = servicios
        
        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        return context



#devuelve los detalles de una pista
class PistaDetailView(DetailView):
    model = Pista
    template_name = 'pista.html'
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['LANGUAGES'] = [
                ('es', _('Spanish')),
                ('en', _('English')),
            ]
            return context
        
#devuelve los detalles de un servicio
class ServicioDetailView(DetailView):
    model = Servicio
    template_name = 'servicio.html'

    def get_context_data(self, **kwargs):
        #context = super(ServicioDetailView,self).get_context_data(**kwargs)
        #context['estaciones'] = Estacion.objects.filter(servicios=self.object)
        #return context

        context = super().get_context_data(**kwargs)
        context['estaciones'] = Estacion.objects.filter(servicios=self.object)
        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        return context

#formulario
class FormularioView(View):
    template_name = 'formulario.html'

    def get(self, request, *args, **kwargs):
        formulario = MiFormulario()
        context = {'formulario':formulario}
        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        formulario = MiFormulario(request.POST)
        if formulario.is_valid():
            datos_formulario = formulario.cleaned_data
            # Realizar acciones con estos datos, como guardarlos en la BD, enviar un correo, etc. MIRAR ESTO!
            return redirect('index')
        context = {'formulario':formulario}
        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        
        return render(request, self.template_name, context)

 





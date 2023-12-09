from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Localidad, Estacion, Pista, Servicio, EstacionServicio
from .forms import vFormulario 
from django.views.generic import DetailView, ListView, View
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# VISTAS BASADAS EN CLASES
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
     

# devuelve el listado de localidades
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

# devuelve listado de estaciones
class EstacionesListView(ListView):
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
    

# devuelve listado de pistas
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

# devuelve listado de servicios
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

# devuelve las estaciones de cada localidad
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
    

# devuelve los datos de una estacion
class EstacionDetailView(DetailView):
    model = Estacion
    template_name = 'estacion.html'

    def get_context_data(self, **kwargs):
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



# devuelve los detalles de una pista
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
    
# devuelve los detalles de un servicio
class ServicioDetailView(DetailView):
    model = Servicio
    template_name = 'servicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estaciones'] = Estacion.objects.filter(servicios=self.object)
        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        return context

# formulario
class FormularioView(View):
    template_name = 'formulario.html'
    confirmacion_template = 'confirmacion.html'
    
    def get(self, request, *args, **kwargs):
        formulario = vFormulario()
        # traducción
        formulario.fields['nombre'].label = _('Nombre:')
        formulario.fields['apellidos'].label = _('Apellidos:')
        formulario.fields['telefono'].label = _('Telefono:')
        formulario.fields['edad'].label = _('Edad:')
        formulario.fields['direccion'].label = _('Direccion:')
        formulario.fields['email'].label = _('Email:')
        formulario.fields['tipo_viaje'].label = _('Tipo de viaje:')
        formulario.fields['tipo_viaje'].choices = [
            ('default', _('---')),
            ('colegio', _('Colegio')),
            ('universidad', _('Universidad')),
            ('empresa', _('Empresa')),
            ('grupo_amigos', _('Grupo de amigos')),
            ('otros', _('Otros')),
        ]
         
        context = {'formulario':formulario}
        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        formulario = vFormulario(request.POST)

        if formulario.is_valid():
            nuevo_usuario = formulario.save(commit=False)  # aqui coge los datos del formulario pero no los guarda aún en la BD
            nuevo_usuario.save()  # guardar los datos en BD
            
            # redirige la pagina 
            return HttpResponseRedirect(reverse('confirmacion'))  # Cambia 'confirmacion' por el nombre de tu URL de confirmación
        
        context = {'formulario': formulario}
        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        return render(request, self.template_name, context)
        
       
class ConfirmacionView(View):
    conf_template = 'confirmacion.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.conf_template, context)

    def get_context_data(self, **kwargs):
        context = {}
        context['LANGUAGES'] = [
            ('es', _('Spanish')),
            ('en', _('English')),
        ]
        return context
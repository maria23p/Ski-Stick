from django import forms
# para la traducción
from django.utils.translation import gettext as _


class MiFormulario(forms.Form):
    nombre = forms.CharField(label=_("Nombre:"), max_length=100)
    apellidos = forms.CharField(label=_("Apellidos:"), max_length=150)
    telefono = forms.CharField(label=_("Telefono:"), max_length=100)
    edad = forms.IntegerField(label=_("Edad:"))
    direccion =  forms.CharField(label=_("Direccion:"))
    email = forms.EmailField(label=_("Email:"), required = False)
    TIPO_VIAJE_CHOICES = [
        ('default', '---'),
        ('colegio', _('Colegio')),
        ('universidad', _('Universidad')),
        ('empresa', _('Empresa')),
        ('grupo_amigos', _('Grupo de amigos')),
    ]

    tipo_viaje = forms.ChoiceField(label=_("Tipo de viaje:"), choices=TIPO_VIAJE_CHOICES)
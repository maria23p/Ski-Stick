from django import forms

class MiFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre:", max_length=100)
    apellidos = forms.CharField(label="Apellidos:", max_length=150)
    telefono = forms.CharField(label="Telefono:", max_length=100)
    edad = forms.IntegerField(label="Edad:")
    direccion =  forms.CharField(label="Direccion:")
    email = forms.EmailField(label="Email:", required = False)
    TIPO_VIAJE_CHOICES = [
        ('default', '---'),
        ('colegio', 'Colegio'),
        ('universidad', 'Universidad'),
        ('empresa', 'Empresa'),
        ('grupo_amigos', 'Grupo de amigos'),
    ]

    tipo_viaje = forms.ChoiceField(label="Tipo de viaje:", choices=TIPO_VIAJE_CHOICES)
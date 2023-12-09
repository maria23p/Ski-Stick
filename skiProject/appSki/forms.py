from django import forms
# se define los campos que queremos que salgan en el formulario
class vFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre:", max_length=50, min_length=3 )
    apellidos = forms.CharField(label="Apellidos:", max_length=150, min_length=3)
    telefono = forms.CharField(label="Telefono:", max_length=100)
    edad = forms.IntegerField(label="Edad:", min_value=1)
    direccion =  forms.CharField(label="Direccion:", required = False)
    email = forms.EmailField(label="Email:")
    TIPO_VIAJE_CHOICES = [
        ('default', '---'),
        ('colegio', 'Colegio'),
        ('universidad', 'Universidad'),
        ('empresa', 'Empresa'),
        ('grupo_amigos', 'Grupo de amigos'),
    ]

    tipo_viaje = forms.ChoiceField(label="Tipo de viaje:", choices=TIPO_VIAJE_CHOICES, initial='default')
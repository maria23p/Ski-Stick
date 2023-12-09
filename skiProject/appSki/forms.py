from django import forms
from .models import ViajesEnGrupo

class vFormulario(forms.ModelForm):
    class Meta:
        model = ViajesEnGrupo
        fields = ['nombre', 'apellidos', 'telefono', 'edad', 'direccion', 'email', 'tipo_viaje']
        
    # Validación de datos
    # funciones para crear 'restricciones' al introducir los datos (el usuario)
    # hay que usar metodo clean()
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) <= 2 or len(nombre) > 30:
            raise forms.ValidationError("El nombre debe tener entre 2 y 30 caracteres.")
        return nombre
    
    def clean_apellidos(self):
        apellidos = self.cleaned_data['apellidos']
        if len(apellidos) <= 2 or len(apellidos) > 30:
            raise forms.ValidationError("Los apellidos deben tener entre 2 y 30 caracteres.")
        return apellidos
    
    def clean_edad(self):
        edad = self.cleaned_data['edad']
        if edad <= 15 or edad > 90:
            raise forms.ValidationError("La edad debe estar entre 15 y 90 años.")
        return edad

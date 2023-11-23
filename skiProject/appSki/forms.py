from django import forms

class MiFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellidos = forms.CharField(label="Apellidos", max_length=150)
    telefono = forms.CharField(label="Telefono", max_length=100)
    edad = forms.IntegerField(label="Edad")
    direccion =  forms.CharField(label="Direccion")
    email = forms.EmailField(label="Email", required = False)
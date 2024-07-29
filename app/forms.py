from django import forms
from .models import Publicacion, Cliente, Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['nombre', 'descripcion', 'fecha']
        
class BuscadorCliente(forms.Form):
    cliente = forms.CharField()

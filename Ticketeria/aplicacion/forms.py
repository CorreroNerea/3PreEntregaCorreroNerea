from django import forms

class PerfilForm(forms.Form):
    nombre = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    phoneNumber = forms.IntegerField(required=True)
    direccion = forms.CharField(max_length=50, required=True)
    
class CompraForm(forms.Form):
    producto = forms.CharField(max_length=20, required=True)
    codigo = forms.IntegerField(required=True)
    
class ArtistaForm(forms.Form):
    nombreArtista = forms.CharField(max_length=20, required=True)
    descripcion = forms.CharField(max_length=500, required=True)
    
class ProximaFechaForm(forms.Form):
    artista = forms.CharField(max_length=20, required=True)
    date = forms.DateTimeField(required=True)
    lugar = forms.CharField(max_length=20, required=True)
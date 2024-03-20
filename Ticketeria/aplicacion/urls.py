from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('perfil', perfil, name="Perfil"),
    path('compra', compra, name="Compra"),
    path('proximafecha', proximafecha, name="Proximafecha"),
    path('artista', artista, name="Artista"),
    
    #url , funcion, index
    
    path('perfilForm', perfilForm, name="PerfilForm"),
    path('compraForm', compraForm, name="CompraForm"),
    path('ArtistaForm', artistaForm, name="ArtistaForm"),
    path('ProximaFechaForm', proximafechaForm, name="ProximaFechaForm"),

    path('Buscar', buscar, name="buscar"),
    path('encontrarArtista', encontrarArtista, name="encontrarArtista"),
]
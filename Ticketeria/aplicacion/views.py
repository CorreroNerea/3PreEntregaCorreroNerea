from django.shortcuts import render

from .models import *
from .forms import *


def home(request):
    return render(request, "aplicacion/index.html")

def perfil(request):
    contexto = { 'Perfil': Perfil.objects.all() }
    return render(request, "aplicacion/perfil.html", contexto)

def compra(request):
    contexto = { 'Compra': Compra.objects.all() }
    return render(request, "aplicacion/compra.html", contexto)

def artista(request):
    contexto = { 'Artista': Artista.objects.all() }
    return render(request, "aplicacion/artista.html", contexto)

def proximafecha(request):
    contexto = { 'ProximaFecha': ProximaFecha.objects.all() }
    return render(request, "aplicacion/proximafecha.html", contexto)



def perfilForm(request):
    if request.method == "POST":
        miForm = PerfilForm(request.POST)
        if miForm.is_valid():
            perfil_nombre = miForm.cleaned_data.get("nombre")
            perfil_email = miForm.cleaned_data.get("email")
            perfil_phoneNumber = miForm.cleaned_data.get("phoneNumber")
            perfil_direccion = miForm.cleaned_data.get("direccion")
            perfil = Perfil(nombre=perfil_nombre, email=perfil_email, phoneNumber=perfil_phoneNumber, direccion=perfil_direccion)
            perfil.save()
            return render(request, "aplicacion/perfil.html")
    else:
        miForm = PerfilForm()
    return render(request, "aplicacion/perfilForm.html", {"form": miForm} )


def compraForm(request):
    if request.method == "POST":
        miForm = CompraForm(request.POST)
        if miForm.is_valid():
            compra_producto = miForm.cleaned_data.get("producto")
            compra_codigo = miForm.cleaned_data.get("codigo")
            compra = Compra(producto=compra_producto, codigo=compra_codigo)
            compra.save()
            
            contexto = {'compra': Compra.objects.all()}
            return render(request, "aplicacion/compra.html", contexto)
    else:
        miForm = CompraForm()
    return render(request, "aplicacion/compraForm.html", {"form": miForm} )


def artistaForm(request):
    if request.method == "POST":
        miForm = ArtistaForm(request.POST)
        if miForm.is_valid():
            artista_nombreArtista = miForm.cleaned_data.get("nombreArtista")
            artista_descripcion = miForm.cleaned_data.get("descripcion")
            artista = Artista(nombreArtista=artista_nombreArtista, descripcion=artista_descripcion)
            artista.save()
            
            contexto = {'artista': Artista.objects.all()}
            return render(request, "aplicacion/artista.html", contexto)
    else:
        miForm = ArtistaForm()
    return render(request, "aplicacion/artistaForm.html", {"form": miForm} )


def proximafechaForm(request):
    if request.method == "POST":
        miForm = ProximaFechaForm(request.POST)
        if miForm.is_valid():
            proximafecha_artista = miForm.cleaned_data.get("artista")
            proximafecha_date = miForm.cleaned_data.get("date")
            proximafecha_lugar = miForm.cleaned_data.get("lugar")
            proximafecha = ProximaFecha(artista=proximafecha_artista, date=proximafecha_date, lugar=proximafecha_lugar)
            proximafecha.save()
            return render(request, "aplicacion/proximafecha.html")
    else:
        miForm = ProximaFechaForm()
    return render(request, "aplicacion/proximafecha.html", {"form": miForm} )


def buscar(request):
    return render(request, "aplicacion/buscar.html")

def encontrarArtista(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        artista = Artista.objects.filter(nombreArtista__icontains=patron)
        contexto = {"artista": artista}
        return render(request, "aplicacion/artista.html", contexto)
    
    contexto = { 'Artista': Artista.objects.all() }
    return render(request, "aplicacion/artista.html", contexto)

# Create your views here.

from django.db import models

class Perfil(models.Model):
    nombre = models.CharField(max_length=20)
    email = models.EmailField()
    phoneNumber = models.IntegerField()
    direccion = models.CharField(max_length=50)

class Compra(models.Model):
    producto = models.CharField(max_length=20)
    codigo = models.IntegerField()
    
class Artista(models.Model):
    nombreArtista = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=500)
    
class ProximaFecha(models.Model):
    artista = models.CharField(max_length=20)
    date = models.DateTimeField()
    lugar = models.CharField(max_length=20)

from django.db import models

#JesusGonzalez_20150903: Creamos las primeras clases del model
#doc e info: https://docs.djangoproject.com/en/1.8/topics/db/models/

class Restaurantes(models.Model):
    restaurante_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    nombre =  models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    mapa = models.CharField(max_length=255)
    descripcion = models.TextField()
    codigoPostal = models.IntegerField(null=True)
    baja_logica = models.SmallIntegerField(null=True)
    fecha_alta = models.DateTimeField()
    fecha_baja = models.DateTimeField(null=True)

class Restaurantes_fotos(models.Model): 
    restaurante_foto_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    restaurante = models.ForeignKey(Restaurantes) #clave foranea
    nombre = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
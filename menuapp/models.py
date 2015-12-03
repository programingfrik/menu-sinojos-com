from django.db import models

#JesusGonzalez_20150903: Creamos las primeras clases del model
#doc e info: https://docs.djangoproject.com/en/1.8/topics/db/models/

class Restaurantes(models.Model):
    restaurante_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    nombre =  models.CharField(max_length=255)
    email = models.EmailField(max_length=254) # LuisPv: He cambiado models.CharField por un EmailField.
    direccion = models.CharField(max_length=255)
    mapa = models.CharField(max_length=255)
    descripcion = models.TextField()
    codigoPostal = models.IntegerField(null=True)
    baja_logica = models.SmallIntegerField(null=True)
    fecha_alta = models.DateField(auto_now=False)
    fecha_baja = models.DateField(auto_now=False)

class Restaurantes_fotos(models.Model): 
    restaurante_foto_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    restaurante = models.ForeignKey(Restaurantes) #clave foranea Restaurantes
    nombre = models.CharField(max_length=255)
    #Creo que aqui se podria utilizar el campo ImageField. 
    url = models.CharField(max_length=255)

#LuisEnriquePeña_20150911: Termino todas las clases del model

class Menus(models.Model):
    menu_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    restaurante = models.ForeignKey(Restaurantes) #clave foranea Restaurantes
    platos = models.ForeignKey("Platos") #clave foranea Platos
    nombre_mn = models.CharField(max_length=255)
    visible = models.BooleanField(default=False)
    
class Horarios(models.Model):
    horario_id = models.IntegerField(primary_key=True) #Clave primaria horario
    restaurante = models.ForeignKey(Restaurantes) #clave foranea Restaurantes
    dia = models.ForeignKey("Dia") #clave foranea Dia
    hora_apertura = models.TimeField(auto_now=False)    #LuisPv: Sobre este campo tengo mis dudas
    hora_cierre = models.TimeField(auto_now=False)      #LuisPv: Sobre este campo tengo mis dudas
    
class Dia(models.Model):
    dia_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    nombre_dia = models.CharField(max_length=255) # Aqui no se si utilizar el DateField. 

class Platos(models.Model):
    Plato_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    nombre_pl = models.CharField(max_length=255)
    descripcion_pl = models.CharField(max_length=255)
    baja_logica_pl = models.SmallIntegerField(null=True)
    existencia = models.CharField(max_length=255) #No se que quiere decir "existencia" ??? Un boolean tal ves 
    
class Pedidos(models.Model):
    Pedidos_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    restaurante = models.ForeignKey(Restaurantes) #clave foranea Restaurantes
    usuarios = models.ForeignKey("Usuarios") #clave foranea usuario_id
    fecha_pedido = models.DateField(auto_now=False)
    hora_pedido = models.TimeField(auto_now=False)  #LuisPv: Sobre este campo tengo mis dudas
    total_pedido = models.DecimalField(max_digits=12, decimal_places=2) 
    estado_pedido = models.CharField(max_length=254)

class Puntaje_restaurante(models.Model):
    puntaje_restaurante_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    restaurante = models.ForeignKey(Restaurantes) #clave foranea Restaurantes
    usuarios = models.ForeignKey("Usuarios") #clave foranea usuario_id
    puntaje = models.ForeignKey("Puntaje") #clave foranea puntaje_id
    
class Platos_fotos(models.Model):
    platos_foto_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    platos = models.ForeignKey(Platos) #clave foranea Platos
    nombre_plato = models.CharField(max_length = 254)
    img_plato = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100) #Aqui me arriesgo a utililzarlo pendiente definir
    url_plato = models.URLField(max_length=254) # Para utilizar el URLField
    
class Pedidos_platos(models.Model):
    pedido_plato_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    platos = models.ForeignKey(Platos) #clave foranea Plato_id
    #precio_plato = models.DecimalField(max_digits=None, decimal_places=None) #Aqui algo no cuadra, ya ponemos el precio en la tabla "Platos_precios"
    cantidad_platos = models.IntegerField(null=True)
    Pedidos = models.ForeignKey(Pedidos) #clave foranea Pedidos_id
    
class Platos_precios(models.Model):
    plato_precio_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    platos = models.ForeignKey(Platos) #clave foranea Plato_id
    precio_plato = models.DecimalField(max_digits=12, decimal_places=2)

class Puntaje_platos(models.Model):
    Puntaje_platos_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    platos = models.ForeignKey(Platos) #clave foranea Plato_id
    usuarios = models.ForeignKey("Usuarios") #clave foranea usuario_id
    puntaje = models.ForeignKey("Puntaje") #clave foranea puntaje_id
    
class Puntaje(models.Model):
    #Necesito entender bien esta tabla, sera el puntaje de Platos, Restaurantes y Usuarios de todo?? 
    puntaje_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    valor = models.IntegerField()

class Restaurantes_favoritos(models.Model):
    restaurante_favorito_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    restaurante = models.ForeignKey(Restaurantes) #clave foranea restaurante_id
    usuarios = models.ForeignKey("Usuarios") #clave foranea usuario_id
    fecha_fav = models.DateField(auto_now=False)

class Usuarios(models.Model):
    usuario_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    usuario_nombre = models.CharField(max_length = 254)
    usuario_apellido = models.CharField(max_length = 254)
    usuario_password = models.CharField(max_length = 254)
    usuario_direccion = models.CharField(max_length = 254)
    usuario_email = models.EmailField(max_length=254)
    usuario_direccion = models.CharField(max_length=255)
    usuario_codigoPostal = models.IntegerField(null=True)
    fecha_alta = models.DateField(auto_now=False)
    fecha_baja = models.DateField(auto_now=False)
    baja_logica = models.SmallIntegerField(null=True)

class Puntaje_usuarios (models.Model):
    puntaje_usuarios_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    usuarios = models.ForeignKey("Usuarios") #clave foranea usuario_id
    usuarios = models.ForeignKey("Usuarios") #clave foranea usuario_id
    puntaje = models.ForeignKey("Puntaje") #clave foranea puntaje_id

#Realmente no se para que es esta tabla
class Puntaje_tipo_usuario (models.Model):
    puntaje_tipo_usuario_id = models.IntegerField(primary_key=True) #Clave primaria explicita
    tipo = models.CharField(max_length = 254)

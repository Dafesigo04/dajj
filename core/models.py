from tabnanny import verbose
from django.db import models
from django.utils.html import format_html

class Servicio(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre")
    
 
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        db_table = "servicio"
        ordering = ["id"]

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre")
    description = models.TextField(max_length=500,verbose_name="Descripción")
    
 
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "categoria"
        ordering = ["id"]


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')#verbose name hace que aparesca en las vistas con un nombre que le damos 
    description = models.TextField(max_length=500, verbose_name='Descripción')
    price = models.IntegerField(verbose_name='Precio')
    quanty = models.IntegerField(verbose_name='Cantidad')
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    foto = models.ImageField("Imagen del producto",upload_to="media")

    def Imagen_Product(self):
        return format_html ( '<img src= {} width="130" height="100" />', self.foto.url)
    


    def __str__(self):
       return self.name     #es para devolver el nombre del producto

    class Meta:     #Define los metadatos del modelo
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']

class Supplier(models.Model):
    rut = models.CharField(max_length=150, verbose_name='Rut')
    name = models.CharField(max_length=150, verbose_name='Nombre')#verbose name hace que aparesca en las vistas con un nombre que le damos 
    direction = models.TextField(max_length=500, verbose_name='Dirección')
    number = models.IntegerField(verbose_name='Telefono')


    def __str__(self):
       return self.name     #es para devolver el nombre del producto

    class Meta:     #Define los metadatos del modelo
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedor'
        ordering = ['id']


class Schedule(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre Empleado")
    apellido = models.TextField(max_length=500,verbose_name="Apellido")
    cedula = models.IntegerField(verbose_name='N° de documento')
    servicio = models.ManyToManyField(Servicio)
    horaen = models.CharField(max_length=7, verbose_name='Hora entrada')
    horasal = models.CharField(max_length=7, verbose_name='Hora Salida')
    
 
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"
        db_table = "horario"
        ordering = ["id"]


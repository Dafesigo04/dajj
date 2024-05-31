from django.db import models

# Create your models here.

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    foto = models.ImageField("Foto",upload_to="media")
    nombre = models.CharField(max_length=150, verbose_name='Nombres') 

    def __str__(self):
        return self.nombre

    def delete(self, using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()

    
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        db_table = "cervicio"
        ordering = ["id"]

class Empleado(models.Model):
     id = models.AutoField(primary_key=True)
     foto = models.ImageField("Foto",upload_to="media") 
     name = models.CharField(max_length=150, verbose_name="Nombre") 
     apellido = models.CharField(max_length=150, verbose_name="Apellido") 
     jornada = models.CharField(max_length=18, verbose_name="Jornada")
     disponibilidad = models.CharField(max_length=150, verbose_name="Disponivilidad")
     servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, verbose_name="Servicio")  
     
     def __str__(self): 
        fila ="Nombre: " + self.name + " - " + "Apellido: " + self.apellido 
        return fila

     def delete(self, using=None, keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()

class Citas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, verbose_name='Nombres')
    apellido = models.CharField(max_length=150, verbose_name='Apellidos')
    correo = models.EmailField(max_length=40, verbose_name='Correo')
    documento = models.IntegerField(verbose_name='N° de documento')
    fecha = models.DateField(verbose_name='Fecha')
    hora = models.CharField(max_length=10, verbose_name='Hora')
    estilista = models.CharField(max_length=70, verbose_name='Estilista')
    servicio = models.CharField(max_length=100, verbose_name="Servicio", null=True)

    def __str__(self):
        fila ="Nombres: " + self.nombre + " - " + "Apellidos: " + self.apellido + " - " + "Correo: " + self.correo  + " - " + "Servicio: " + self.servicio
        return fila

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        db_table = "cita"
        ordering = ["id"]

class Dia(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombres')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Dia"
        verbose_name_plural = "Dias"
        db_table = "dia"
        ordering = ["id"]



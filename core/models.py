from django.db import models

# Create your models here.

class Raza(models.Model):
    nombre= models.CharField(max_length= 20)
    descripcion= models.CharField(max_length=200)

class Estado(models.Model):
    nombre= models.CharField(max_length= 20)
    descripcion= models.CharField(max_length=200)

class Mascota(models.Model):
    nombre= models.CharField(max_length= 40)
    raza= models.ForeignKey(Raza, on_delete = models.CASCADE)
    genero= models.CharField(max_length= 1)
    fechaIngreso= models.IntegerField()
    fechaNac= models.IntegerField()
    descripcion= models.CharField(max_length=200)
    estado= models.ForeignKey(Estado, on_delete = models.CASCADE)
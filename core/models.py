from django.db import models

# Create your models here.

class Raza(models.Model):
    nombre= models.CharField(max_length= 20)
    descripcion= models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre= models.CharField(max_length= 20)
    descripcion= models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    nombre= models.CharField(max_length= 40)
    raza= models.ForeignKey(Raza, on_delete = models.CASCADE)
    genero= models.CharField(max_length= 1)
    fechaIngreso= models.CharField(max_length=20)
    fechaNac= models.CharField(max_length=20)
    descripcion= models.CharField(max_length=200)
    estado= models.ForeignKey(Estado, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"
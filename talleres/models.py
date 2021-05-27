from django.db import models

# Create your models here.


class Administradores(models.Model):
	id_admin = models.AutoField(primary_key=True)
	contrasena = models.CharField(max_length=32)
	nombre = models.CharField(max_length=32)
	apellido_paterno = models.CharField(max_length=32, null=True)
	apellido_materno = models.CharField(max_length=32 , null=True)
	email = models.EmailField()
	num_telefono = models.BigIntegerField()
	tipo = models.CharField(max_length=32)

	def __str__(self):
		return (self.nombre)

class Talleres(models.Model):
	id_taller = models.AutoField(primary_key = True)
	id_admin = models.ForeignKey(Administradores, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=32)

	def __str__(self):
		return (self.nombre)

class Alumnos(models.Model):
	num_control = models.CharField(max_length=10)
	id_taller = models.ForeignKey(Talleres, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=32)
	apellido_paterno = models.CharField(max_length=32, null=True)
	apellido_materno = models.CharField(max_length=32, null=True)
	carrera = models.CharField(max_length=32) 
	grupo = models.CharField(max_length=10)
	email = models.EmailField()
	num_telefono = models.BigIntegerField()

	def __str__(self):
		return (self.nombre)



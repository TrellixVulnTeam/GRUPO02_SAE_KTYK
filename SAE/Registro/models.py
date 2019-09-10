from django.db import models
from django.db.models.signals import post_save

class Colegio(models.Model):
	nombre=models.CharField(max_length=20)
	comuna=models.CharField(max_length=20)
	direccion=models.CharField(max_length=20)
	colegios=models.Manager()

	def __str__(self):
		return "{}".format(self.nombre)

class Profesor(models.Model):
	rut=models.CharField(max_length=10)
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	fechanacimiento=models.DateTimeField()
	profesores=models.Manager()

	def __str__(self):
		return "{}".format(self.nombre)

def crear_profesor(sender,instance,**kwargs):
	print(instance.rut)

post_save.connect(crear_profesor,sender=Profesor)

class Curso(models.Model):
	nombrecurso=models.CharField(max_length=20)
	cupos=models.PositiveIntegerField()
	profesorjefe=models.ForeignKey(Profesor,on_delete=models.CASCADE)
	colegio= models.ForeignKey(Colegio,on_delete=models.CASCADE)
	cursos=models.Manager()

	def __str__(self):
		return "{}".format(self.nombrecurso)

class Alumno(models.Model):
	rut=models.CharField(max_length=10)
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	fechanacimiento=models.DateTimeField()
	curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
	alumno=models.Manager()

	def __str__(self):
		return "{}".format(self.rut)

class Asignatura(models.Model):
	nombre_asignatura=models.CharField(max_length=20)
	nivel=models.CharField(max_length=20)
	curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
	
	def __str__(self):
		return "{}".format(self.nombre)
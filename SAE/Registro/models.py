from django.db import models
#from django.db.models.signal import post_save

class Colegio(models.Model):
	nombre=models.CharField(max_length=20)
	comuna=models.CharField(max_length=20)
	direccion=models.CharField(max_length=20)
	colegios=models.Manager()

	def __str__(self):
		return "{}".format(self.nombre)

class Prosefor(models.Model):
	rut=models.CharField(max_length=10)
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	fechanacimiento=models.DateTimeField()
	profesor=models.Manager()

	def __str__(self):
		return "{}".format(self.nombre)


class Curso(models.Model):
	nombrecurso=models.CharField(max_length=20)
	cupos=models.PositiveIntegerField()
	profesorjefe=models.ForeignKey(Prosefor,on_delete=models.CASCADE)
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
	curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
	
	def __str__(self):
		return "{}".format(self.nombre)
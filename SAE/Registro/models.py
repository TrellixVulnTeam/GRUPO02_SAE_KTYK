from django.db import models

class Colegio(models.Model):
	nombre=models.CharField(max_length=20)
	comuna=models.CharField(max_length=20)
	direccion=models.CharField(max_length=20)
	colegios=models.Manager()

	def __str__(self):
		return "{}".format(self.nombre)
		
class Curso(models.Model):
	nombrecurso=models.CharField(max_length=20)
	cupos=models.PositiveIntegerField()
	profesorjefe=models.CharField(max_length=20)
	colegio= models.ForeignKey(Colegio,on_delete=models.CASCADE)
	cursos=models.Manager()

	def __str__(self):
		return "{}".format(self.nombrecurso)
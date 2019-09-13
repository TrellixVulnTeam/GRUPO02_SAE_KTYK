from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Colegio(models.Model):
	nombre=models.CharField(max_length=20)
	comuna=models.CharField(max_length=20)
	direccion=models.CharField(max_length=20)
	colegios=models.Manager()

	def __str__(self):
		return "{}".format(self.nombre)

class Maestra(models.Model):
	rut_alumno = models.CharField(max_length=10)
	tipo_de_permiso = models.PositiveIntegerField();
	def __str__(self):
		return "{}".format(self.rut_alumno)

class Curso(models.Model):
	nombrecurso=models.CharField(max_length=20)
	codigo_curso=models.CharField(max_length=4)
	#profesorjefe=models.ForeignKey(Profesor,on_delete=models.models.CASCADE)
	colegio= models.ForeignKey(Colegio,on_delete=models.CASCADE)
	cursos=models.Manager()

	def __str__(self):
		return "{}".format(self.codigo_curso)

class Alumno(models.Model):
	rut=models.CharField(max_length=10)
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	fechanacimiento=models.DateTimeField()
	curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
	sexo = models.PositiveIntegerField()
	alumno=models.Manager()

	def __str__(self):
		return "{}".format(self.rut)

class Apoderados(models.Model):
	rut=models.CharField(max_length=10)
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	fechanacimiento=models.DateTimeField()
	sexo = models.PositiveIntegerField()
	alumnos = models.ForeignKey(Alumno,on_delete=models.CASCADE)
	apoderados=models.Manager()

	def __str__(self):
		return "{}".format(self.nombre)

class Asignatura(models.Model):
	nombre_asignatura=models.CharField(max_length=20)
	codigo=models.CharField(max_length=4)
	curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
	
	def __str__(self):
		return "{}".format(self.codigo)

class Profesor(models.Model):
	rut=models.CharField(max_length=10)
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	fechanacimiento=models.DateTimeField()
	sexo = models.PositiveIntegerField()
	asignaturas = models.ForeignKey(Asignatura,on_delete=models.CASCADE)
	responsabilidad = models.BooleanField()
	colegio_pertenece = models.ForeignKey(Colegio,on_delete=models.CASCADE)
	profesores=models.Manager()

	def __str__(self):
		return "{}".format(self.nombre)

def crear_profesor(sender,instance,**kwargs):
	if sender.responsabilidad== True:
		user = User.objects.create_user(instance.nombre[0]+'.'+instance.apellido, instance.nombre+'@colegio.com', instance.rut)
		user.first_name=0
		user.save()
	else:
		user = User.objects.create_user(instance.nombre[0]+'.'+instance.apellido, instance.nombre+'@colegio.com', instance.rut)
		user.first_name=1
		user.save()


post_save.connect(crear_profesor,sender=Profesor)

def crear_alumno(sender,instance,**kwargs):
	user = User.objects.create_user(instance.nombre[0]+'.'+instance.apellido, instance.nombre+'@colegio.com', instance.rut)
	user.first_name=2
	user.save()

post_save.connect(crear_alumno,sender=Alumno)

class Actividades(models.Model):
	codigo_actividades = models.CharField(max_length=4)
	nombre = models.CharField(max_length=10)
	asignatura = models.ForeignKey(Asignatura,on_delete=models.CASCADE)

	def __str__(self):
		return "{}".format(self.codigo_actividades)

class Notas(models.Model):
	rut_alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)
	nota = models.PositiveIntegerField()
	codigo_actividad = models.ForeignKey(Actividades,on_delete=models.CASCADE)

	def __str__(self):
		return "{}".format(self.rut_alumno)
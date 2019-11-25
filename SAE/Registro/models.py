from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from multiselectfield import MultiSelectField

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
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	rut=models.CharField(max_length=10)
	usercreado=models.PositiveIntegerField(default=0, blank=True, null=True)
	tipouser=models.PositiveIntegerField(blank=True, null=True)
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	fechanacimiento=models.DateTimeField()
	curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
	sexo = models.CharField(max_length=1,choices=GENDER_CHOICES)
	alumno=models.Manager()

	def __str__(self):
		return "{}".format(self.rut)

class Apoderados(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	rut=models.CharField(max_length=10)
	nombre=models.CharField(max_length=20)
	usercreado=models.PositiveIntegerField(default=0, blank=True, null=True)
	apellido=models.CharField(max_length=20)
	fechanacimiento=models.DateTimeField()
	sexo = models.CharField(max_length=1,choices=GENDER_CHOICES)
	alumnos = models.ForeignKey(Alumno,on_delete=models.CASCADE)
	apoderados=models.Manager()

	def __str__(self):
		return "{}".format(self.nombre)

class Profesor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	rut=models.CharField(max_length=10)
	tipouser=models.PositiveIntegerField(blank=True, null=True)
	usercreado=models.PositiveIntegerField(default=0, blank=True, null=True)
	nombre=models.CharField(max_length=20)
	apellido=models.CharField(max_length=20)
	fechanacimiento=models.DateTimeField()
	sexo = models.CharField(max_length=1,choices=GENDER_CHOICES)
	responsabilidad = models.BooleanField()
	colegio_pertenece = models.ForeignKey(Colegio,on_delete=models.CASCADE)
	profesores=models.Manager()

	def __str__(self):
		return "{}".format(self.rut)

class Asignatura(models.Model):
	materias= (
        ('leg', 'Lenguaje'),
        ('mat', 'Matematicas'),
        ('his', 'Historia'),
        ('fis', 'Fisica'),
        ('qui', 'Quimica'),
        ('bio', 'Biologia'),
        ('ing', 'Ingles'),
    )
	nombre_asignatura=models.CharField(max_length=20)
	codigo=models.CharField(max_length=4)
	curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
	profesor=models.ForeignKey(Profesor,on_delete=models.CASCADE)
	unidades=models.PositiveIntegerField(default=0, blank=True, null=True)
	materia=models.CharField(max_length=3,choices=materias, blank=True, null=True)
	asignaturas= models.Manager()

	def __str__(self):
		return "{}".format(self.codigo)



def crear_profesor(sender,instance,**kwargs):
	if instance.usercreado == 0:

		if sender.responsabilidad== True:
			user = User.objects.create_user(instance.nombre[0]+'.'+instance.apellido, instance.rut, instance.rut)
			user.first_name=0
			user.last_name=instance.colegio_pertenece
			user.save()
			instance.user=User.objects.last()
			instance.tipouser=0
			instance.usercreado=1
			instance.save()
		else:
			user = User.objects.create_user(instance.nombre[0]+'.'+instance.apellido, instance.rut, instance.rut)
			user.first_name=1
			user.last_name=instance.colegio_pertenece
			user.save()
			instance.user=User.objects.last()
			instance.tipouser=1
			instance.usercreado=1
			instance.save()


post_save.connect(crear_profesor,sender=Profesor)

def crear_alumno(sender,instance,**kwargs):
	if instance.usercreado == 0:
		user = User.objects.create_user(instance.nombre[0]+'.'+instance.apellido, instance.rut, instance.rut)
		user.first_name=2
		user.save()
		instance.user=User.objects.last()
		instance.tipouser=2
		instance.usercreado=1
		instance.save()

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


class Puntaje(models.Model):
	codigo_actividad = models.PositiveIntegerField()
	alumno = models.ForeignKey(Alumno,on_delete=models.CASCADE, blank=True, null=True)
	acomulado = models.CharField(max_length=3)

class Unidad(models.Model):
	nombre=models.CharField(max_length=10)
	asignatura=models.ForeignKey(Asignatura,on_delete=models.CASCADE, blank=True, null=True)
	lvls=models.PositiveIntegerField(default=0, blank=True, null=True)
	unidades=models.Manager()

class Nivel(models.Model):
	nombre=models.CharField(max_length=10)
	unidad=models.ForeignKey(Unidad,on_delete=models.CASCADE, blank=True, null=True)
	niveles=models.Manager()
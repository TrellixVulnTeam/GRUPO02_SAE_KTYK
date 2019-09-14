from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView,ListView
from .models import *
from quiz.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#clases Colegio
class ColegioCreate(CreateView):
	model = Colegio
	template_name = './colegio_form.html'
	fields = '__all__'

class ColegioUpdate(UpdateView):
	model = Colegio
	template_name = './colegio_form.html'
	fields = ['nombre', 'comuna', 'direccion']

class ColegioDelete(DeleteView):
	model = Colegio
	template_name = './colegio_confirm_delete.html'
	success_url = reverse_lazy('Colegios')

#Clases Alumnos
class AlumnoCreate(CreateView):
	model = Alumno
	template_name = './alumno_form.html'
	fields = '__all__'

class AlumnoUpdate(UpdateView):
	model = Alumno
	template_name = './alumno_form.html'
	fields = '__all__'

class AlumnoDelete(DeleteView):
	model = Alumno
	template_name = './alumno_confirm_delete.html'
	success_url = reverse_lazy('Alumnos')

#Clases Profesor
class ProfesorCreate(CreateView):
	model = Profesor
	template_name = './alumno_form.html'
	fields = '__all__'

class ProfesorUpdate(UpdateView):
	model = Profesor
	template_name = './alumno_form.html'
	fields = '__all__'

class ProfesorDelete(DeleteView):
	model = Profesor
	template_name = './profesor_confirm_delete.html'
	success_url = reverse_lazy('Profesor')

#index
class HomePageView(TemplateView):
	def get(self,request,**kwargs):
		if request.user.is_anonymous == True:
			return render(request,'index.html')
		else:
			if request.user.first_name ==2 :
				return render(request,'index.html',{'alumno':Alumno.alumno.get(rut=request.user.email)})
			else:
				return render(request,'index.html')

#Vista Colegios
class HomeColegiosView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		return render(request,'Colegios.html',{'colegios':Colegio.colegios.all()} )

#Vistas Asignaturas del curso
class HomeAsignaturasCursoView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		nombre = kwargs["pk_curso"]
		return render(request,'asignaturas_curso.html',{'asignaturas':Asignatura.asignaturas.all(),'curso':Curso.cursos.get(id=nombre),'tipo':1})


#Vista Alumnos
class HomeAlumnosView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		nombre = kwargs["pk_curso"]
		return render(request,'Alumnos.html',{'alumno':Alumno.alumno.all(),'curso':Curso.cursos.get(id=nombre),'tipo':1})

class HomeAlumnoDetalleView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		nombre = kwargs["pk_alumno"]
		return render(request,'AlumnoDetalle.html',{'alumno':Alumno.alumno.get(id=nombre)})


class AlumnosView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		return render(request,'Alumnos.html',{'alumno':Alumno.alumno.all(),'tipo':2,'colegio':Colegio.colegios.get(id=request.user.last_name)})

#Vista Profesores
class HomeProfesoresView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		if request.user.first_name ==2:
			return render(request,'Profesores.html',{'profesor':Profesor.profesores.all(),'alumno':Alumno.alumno.get(rut=request.user.email)} )
		else :
			return render(request,'Profesores.html',{'profesor':Profesor.profesores.all()})
#Vista Actividades
class HomeActividadesView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		nombre=kwargs["pk_asignatura"]
		return render(request,'Actividades.html',{'quiz':Quiz.quizz.all(),'asignatura':Asignatura.asignaturas.get(id=nombre)})


class HomeAsignaturasView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		return render(request,'Asignaturas.html',{'asignaturas':Asignatura.asignaturas.all(),'profesor':Profesor.profesores.get(rut=request.user.email)})



#Detalles del colegio / Vista de Cursos de colegio
class DetalleColegioView(LoginRequiredMixin,TemplateView):
	def get(self, request, **kwargs):
		nombre=kwargs["id"]
		return render(request,'colegio.html',{'cursos':Curso.cursos.all(),'colegio': Colegio.colegios.get(id=nombre)})

#Detalles del Curso/ ###Agregar lista de alumnos###
class DetalleCursoView(LoginRequiredMixin,TemplateView):
	def get(self,request,**kwargs):
		nombre=kwargs["pk_curso"]
		return render(request,'curso.html',{'alumno': Alumno.alumno.all(), 'cursos':Curso.cursos.get(id=nombre)})

##Detalles del Profesor
class DetalleProfesorView(LoginRequiredMixin,TemplateView):
	def get(self,request,**kwargs):
		nombre=kwargs["pk_profesor"]
		return render(request,'detalleprofesor.html',{'profesor': Profesor.profesores.get(id=nombre)})

class QuizListView(ListView):
    model = Quiz

    def get_queryset(self):
        queryset = super(QuizListView, self).get_queryset()
        return queryset.filter(draft=False)


class QuizCreate(LoginRequiredMixin,CreateView):
	model = Quiz
	template_name = './curso_form.html'
	fields = '__all__'

##Clases Cursos
class CursoCreate(LoginRequiredMixin,CreateView):
	model = Curso
	template_name = './curso_form.html'
	fields = '__all__'


class CursoUpdate(UpdateView):
	model = Curso
	template_name = './curso_form.html'
	fields = '__all__'

class CursoDelete(DeleteView):
	model = Curso
	template_name = './curso_confirm_delete.html'
	success_url = reverse_lazy('Cursos')

##Clases Cursos
class AsignaturaCreate(LoginRequiredMixin,CreateView):
	model = Asignatura
	template_name = './curso_form.html'
	fields = '__all__'


class AsignaturaUpdate(UpdateView):
	model = Asignatura
	template_name = './curso_form.html'
	fields = '__all__'

class AsignaturaDelete(DeleteView):
	model = Asignatura
	template_name = './curso_confirm_delete.html'
	success_url = reverse_lazy('Cursos')
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Colegio,Curso,Alumno, Profesor
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
		return render(request,'index.html',context=None)

#Vista Colegios
class HomeColegiosView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		return render(request,'Colegios.html',{'colegios':Colegio.colegios.all()} )

#Vista Alumnos
class HomeAlumnosView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		return render(request,'Alumnos.html',{'alumno':Alumno.alumno.all()} )

#Vista Profesores
class HomeProfesoresView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		return render(request,'Profesores.html',{'profesor':Profesor.profesores.all()} )



#Detalles del colegio / Vista de Cursos de colegio
class DetalleColegioView(LoginRequiredMixin,TemplateView):
	def get(self, request, **kwargs):
		nombre=kwargs["id"]
		return render(request,'colegio.html',{'cursos':Curso.cursos.all(),'colegio': Colegio.colegios.get(id=nombre)})

#Detalles del Curso/ ###Agregar lista de alumnos###
class DetalleCursoView(LoginRequiredMixin,TemplateView):
	def get(self,request,**kwargs):
		nombre=kwargs["pk_curso"]
		return render(request,'curso.html',{'curso': Curso.cursos.get(id=nombre)})

##Detalles del Profesor
class DetalleProfesorView(LoginRequiredMixin,TemplateView):
	def get(self,request,**kwargs):
		nombre=kwargs["pk_profesor"]
		return render(request,'detalleprofesor.html',{'profesor': Profesor.profesores.get(id=nombre)})

##Clases Cursos
class CursoCreate(LoginRequiredMixin,CreateView):
	model = Curso
	template_name = './curso_form.html'
	fields = '__all__'

class CursoUpdate(UpdateView):
	model = Curso
	template_name = './curso_form.html'
	fields = ['nombrecurso', 'cupos', 'profesorjefe']

class CursoDelete(DeleteView):
	model = Curso
	template_name = './curso_confirm_delete.html'
	success_url = reverse_lazy('Cursos')
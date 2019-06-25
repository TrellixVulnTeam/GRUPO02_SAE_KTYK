from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Colegio,Curso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ColegioCreate(CreateView):
	print("En create")
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

class HomePageView(TemplateView):
	def get(self,request,**kwargs):
		return render(request,'index.html',context=None)

class HomeColegiosView(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		return render(request,'Colegios.html',{'colegios':Colegio.colegios.all()} )

class DetalleColegioView(LoginRequiredMixin,TemplateView):
	def get(self, request, **kwargs):
		nombre=kwargs["id"]
		return render(request,'colegio.html',{'cursos':Curso.cursos.all(),'colegio': Colegio.colegios.get(id=nombre)})

class DetalleCursoView(LoginRequiredMixin,TemplateView):
	def get(self,request,**kwargs):
		nombre=kwargs["pk_curso"]
		return render(request,'curso.html',{'curso': Curso.cursos.get(id=nombre)})

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
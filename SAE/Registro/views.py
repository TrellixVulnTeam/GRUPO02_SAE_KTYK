from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView,ListView
from .models import *
from quiz.models import *
from multichoice.models import *
from essay.models import *
from true_false.models import *
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


class QuizzCreate(CreateView):
	model = Quiz
	template_name = './colegio_form.html'
	fields = '__all__'

class QuizUpdate(UpdateView):
	model = Quiz
	template_name = './colegio_form.html'
	fields = '__all__'

class QuizDelete(DeleteView):
	model = Quiz
	template_name = './colegio_confirm_delete.html'
	success_url = reverse_lazy('')

class TFCreate(CreateView):
	model = TF_Question
	template_name = './colegio_form.html'
	fields = '__all__'

class TFUpdate(UpdateView):
	model = TF_Question
	template_name = './colegio_form.html'
	fields = '__all__'

class TFDelete(DeleteView):
	model = TF_Question
	template_name = './colegio_confirm_delete.html'
	success_url = reverse_lazy('')

class MCQuestionCreate(CreateView):
	model = MCQuestion
	template_name = './colegio_form.html'
	fields = '__all__'

class MCQuestionUpdate(UpdateView):
	model = MCQuestion
	template_name = './colegio_form.html'
	fields = '__all__'

class MCQuestionDelete(DeleteView):
	model = MCQuestion
	template_name = './colegio_confirm_delete.html'
	success_url = reverse_lazy('')

class Essay_QuestionCreate(CreateView):
	model = Essay_Question
	template_name = './colegio_form.html'
	fields = '__all__'

class Essay_QuestionUpdate(UpdateView):
	model = Essay_Question
	template_name = './colegio_form.html'
	fields = '__all__'

class Essay_QuestionDelete(DeleteView):
	model = Essay_Question
	template_name = './colegio_confirm_delete.html'
	success_url = reverse_lazy('')

class OpcionesMC(CreateView):
	model = Answer
	template_name = './colegio_form.html'
	fields = '__all__'


#Clases Alumnos
class AlumnoCreate(CreateView):
	model = Alumno
	template_name = './alumno_form.html'
	fields = ['nombre','apellido','rut','fechanacimiento','sexo','curso']

class AlumnoCreate2(CreateView):
	model = Alumno
	template_name = './alumno_form.html'
	fields = ['nombre','apellido','rut','fechanacimiento','sexo']

	def form_valid(self,form):
		
		curso = Curso.cursos.get(id=self.kwargs["pk_curso"])
		form.instance.curso = curso
		return super(AlumnoCreate2,self).form_valid(form)	

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

#preguntas
class Preguntas(LoginRequiredMixin, TemplateView):
	def get(self,request,**kwargs):
		return render(request,'preguntas.html')
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

class QuizListView(LoginRequiredMixin,ListView):
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
	fields = ['nombrecurso','codigo_curso']

	def form_valid(self,form):
		
		colegio = Colegio.colegios.get(id=self.kwargs["pk"])
		form.instance.colegio = colegio
		return super(CursoCreate,self).form_valid(form)


class CursoUpdate(UpdateView):
	model = Curso
	template_name = './curso_form.html'
	fields = '__all__'

class CursoDelete(DeleteView):
	model = Curso
	template_name = './curso_confirm_delete.html'
	success_url = reverse_lazy('Cursos')

##Clases Cursos
class QuizCreateNivelacion(CreateView):
	model = Quiz
	template_name = './colegio_form.html'
	fields = '__all__'

class AsignaturaCreate(LoginRequiredMixin,CreateView):

	model = Asignatura
	template_name = './curso_form.html'
	fields = ['nombre_asignatura','codigo','profesor']

	


	def form_valid(self,form):
		idcolegio=self.kwargs["pk_colegio"]
		cursito = Curso.cursos.get(id=self.kwargs["pk_curso"])
		form.instance.curso = cursito
		return super(AsignaturaCreate,self).form_valid(form)

	def get_success_url(self):

		colegioid=self.kwargs["pk_colegio"]
		cursoid=self.kwargs["pk_curso"]
		return reverse_lazy('asignaturas_del_curso',kwargs={"pk_colegio":colegioid,"pk_curso":cursoid})

class AsignaturaUpdate(UpdateView):
	model = Asignatura
	template_name = './curso_form.html'
	fields = '__all__'

class AsignaturaDelete(DeleteView):
	model = Asignatura
	template_name = './curso_confirm_delete.html'
	success_url = reverse_lazy('Cursos')


def DetalleAsignatura(request,pk_colegio,pk_curso,pk_asignatura):
	asignaturas = Asignatura.asignaturas.get(id=pk_asignatura)
	unidades=asignaturas.unidades
	
	if unidades == 0:
		unidadesasignatura=None
	else:
		unidadesasignatura=Unidad.unidades.all()
		unidadesasignatura=unidadesasignatura.filter(asignatura=pk_asignatura)

	if request.POST.get('unidades'):
		unidades = int(request.POST.get('unidades'))
		asignaturas.unidades=1
		asignaturas.save()
		for i in range(unidades):
			unidad= Unidad()
			unidad.nombre= ("Unidad "+str(i+1))
			unidad.asignatura=asignaturas
			unidad.save()

		unidadesasignatura=Unidad.unidades.all()
		unidadesasignatura=unidadesasignatura.filter(asignatura=pk_asignatura)

		
		

	return render(request, "detalleasignaturas.html", {'asignaturas': asignaturas,'unidades':unidades,'unidadesasignatura':unidadesasignatura,'pk_colegio':pk_colegio,'pk_curso':pk_curso,'pk_asignatura':pk_asignatura})

def DetalleUnidad(request,pk_colegio,pk_curso,pk_asignatura,pk_unidad):

	unidad=Unidad.unidades.get(id=pk_unidad)

	if unidad.lvls == 0:
		lvlsunidad=None
	else:
		lvlsunidad=Nivel.niveles.all()
		lvlsunidad=lvlsunidad.filter(unidad=pk_unidad)

	if request.POST.get('niveles'):
		niveles = int(request.POST.get('niveles'))
		unidad.lvls=1
		unidad.save()
		for i in range(niveles):
			nivel= Nivel()
			nivel.nombre= ("Nivel "+str(i+1))
			nivel.unidad=unidad
			nivel.save()

		lvlsunidad=Nivel.niveles.all()
		lvlsunidad=lvlsunidad.filter(unidad=pk_unidad)

	return render(request, "detalleunidad.html", {'lvlsunidad':lvlsunidad,'unidad':unidad,'pk_colegio':pk_colegio,'pk_curso':pk_curso,'pk_asignatura':pk_asignatura})

def DetalleNivel(request,pk_colegio,pk_curso,pk_asignatura,pk_unidad,pk_lvl):


    return render(request,"detallenivel.html")
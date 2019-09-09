from django.conf.urls import url
from django.urls import path,include,re_path
from Registro import views

urlpatterns = [
	url(r'^$',views.HomePageView.as_view(),name="index"),
	url(r'Colegios/',views.HomeColegiosView.as_view(),name="Colegios"),
	url(r'Alumnos/',views.HomeAlumnosView.as_view(),name="Alumnos"),
	re_path(r'^alumno/create/$', views.AlumnoCreate.as_view(success_url='/Alumnos/'), name='alumno_create'),
	re_path(r'^alumno/(?P<pk>\d+)/update/$', views.AlumnoUpdate.as_view(success_url='/Alumnos/'), name='alumno_update'),
	re_path(r'^alumno/(?P<pk>\d+)/delete/$', views.AlumnoDelete.as_view(success_url='/Alumnos/'),name='alumno_delete'),
	re_path(r'^colegio/(?P<id>\d+)/$',views.DetalleColegioView.as_view(),name="detalle"),
	path('accounts/',include('accounts.urls')),
	path('accounts/',include('django.contrib.auth.urls')),
	re_path(r'^colegio/create/$', views.ColegioCreate.as_view(success_url='/Colegios/'), name='colegio_create'),
	re_path(r'^colegio/(?P<pk>\d+)/update/$', views.ColegioUpdate.as_view(success_url='/Colegios/'), name='colegio_update'),
	re_path(r'^colegio/(?P<pk>\d+)/delete/$', views.ColegioDelete.as_view(success_url='/Colegios/'),name='colegio_delete'),
	
	re_path(r'^colegio/(?P<pk_colegio>\d+)/(?P<pk_curso>\d+)/$', views.DetalleCursoView.as_view(), name='detalle_curso'),	
	re_path(r'^colegio/(?P<pk>\d+)/create/', views.CursoCreate.as_view(success_url='/colegio/{colegio_id}'), name='curso_create'),
	re_path(r'^colegio/(?P<pk_colegio>\d+)/(?P<pk>\d+)/update/$', views.CursoUpdate.as_view(success_url='/colegio/{colegio_id}'), name='curso_update'),
	re_path(r'^colegio/(?P<pk_colegio>\d+)/(?P<pk>\d+)/delete/$', views.CursoDelete.as_view(success_url='/colegio/{colegio_id}'),name='curso_delete'),
	
]
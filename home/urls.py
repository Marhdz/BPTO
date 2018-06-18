from django.conf.urls import url, include, static
from django.views.generic import ListView, DetailView
from home.models import Encuesta, Opciones
from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
                url(r'^home/(?P<pk>\d+)$', DetailView.as_view( model = Encuesta, template_name="home/Encuesta.html")),
                path('add/encuesta/', views.encuesta_add, name='encuesta_add'),
                url(r'^add/encuesta/marca_add/$', views.marca_add, name= 'marca_add'),
                url(r'^(?P<pk>\d+)/survey', DetailView.as_view(model = Encuesta, template_name="home/preguntas.html")),
                #url(r'^(?P<pk>\d+)/survey', DetailView.as_view(model = Encuesta, template_name="home/opciones.html")),
                url(r'^$', ListView.as_view(
                                    queryset=Encuesta.objects.all().order_by("-date")[:25],
                                    template_name="home/homeView.html"), name="homepage"),
               ]

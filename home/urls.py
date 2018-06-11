from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from home.models import Encuesta
from . import views

urlpatterns = [
                url(r'^home/(?P<pk>\d+)$', DetailView.as_view(
                                    model = Encuesta,
                                    template_name="home/Encuesta.html")),
                url(r'^add/encuesta$', views.encuesta_add, name='encuesta_add'),
                url(r'^$', ListView.as_view(
                                    queryset=Encuesta.objects.all().order_by("-date")[:25],
                                    template_name="home/homeView.html")),
            ]

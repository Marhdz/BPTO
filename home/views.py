from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import EncuestaForm, MarcaForm
from django.utils import timezone
from django.views.generic import CreateView
from .models import Encuesta, Marca
from django.urls import reverse
from django.views import generic
def index(request):
    return render(request, 'home/homeView.html')


def encuesta_add(request ):
    if request.method == "POST":
        form = EncuestaForm(request.POST)
        if form.is_valid():
             encuesta = form.save(commit=False)
            #encuesta.author = request.user
             encuesta.date = timezone.now()
             encuesta.save()
             return HttpResponseRedirect('marca_add/')
    else:
        form = EncuestaForm()
    return render(request, 'home/encuesta_add.html', {'form': form})

def marca_add(request):
    if request.method == "POST":
        form = MarcaForm(request.POST, request.FILES)
        if form.is_valid():
             marca = form.save(commit=False)
            #encuesta.author = request.user
             marca.save()
             if 'agregar' in request.POST:
                return redirect('/add/marca_add')
             else:
                return HttpResponseRedirect(reverse('homepage'))
    else:
        form = MarcaForm()
    return render(request, 'home/marca.html', {'form': form})

def pregunta(request, encuesta):

    return render(request, 'home/opciones.html', {'pk':[encuesta]})

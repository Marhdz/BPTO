from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import EncuestaForm, MarcaFormSet
from django.db import models
from django.utils import timezone
from django.views.generic import CreateView
from .models import Encuesta, Marca
from django.urls import reverse
from django.forms.models import inlineformset_factory
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
             return HttpResponseRedirect(reverse('homepage'))
    else:
        form = EncuestaForm()
    return render(request, 'home/encuesta_add.html', {'form': form})

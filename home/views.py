from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EncuestaForm
from django.db import models
from django.utils import timezone


def index(request):
    return render(request, 'home/homeView.html')

def encuesta_add(request):
    if request.method == "POST":
        form = EncuestaForm(request.POST)
        if form.is_valid():
            encuesta = form.save(commit=False)
            #encuesta.author = request.user
            encuesta.date = timezone.now()
            encuesta.save()
            return redirect('homeView/')
    else:
        form = EncuestaForm()
    return render(request, 'home/encuesta_add.html', {'form': form})

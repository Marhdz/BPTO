from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import EncuestaForm, MarcaForm
from django.utils import timezone
from django.views.generic import CreateView
from .models import Encuesta, Marca, Persona
from django.urls import reverse
from django.views import generic
from django.db.models import F

def index(request):
    request.session['it']=0
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
             marca.save()
             if 'agregar' in request.POST:
                return redirect('/add/encuesta/marca_add')
             else:
                return HttpResponseRedirect(reverse('homepage'))
    else:
        form = MarcaForm()
    return render(request, 'home/marca.html', {'form': form})

def pregunta(request, pk):
    encuesta=Encuesta.objects.get(pk=pk)
    if request.method == 'POST':
        if 'none' in request.POST:
            request.session['it']=0
            # marcaId=request.POST.get('select','')
            # p=encuesta.marca_set.get(pk=marcaId)
            # p.precioE=0
            # p.save()
            return HttpResponseRedirect(reverse('homepage'))

        if request.session['it']<=encuesta.numIteraciones:
            request.session['it']+=1
            marcaId=request.POST.get('select','')
            p=encuesta.marca_set.get(pk=marcaId)
            p.precioE=p.precioE+encuesta.incremento
            p.votos=p.votos+1
            print(p.votos)
            p.save()

        else:
            print('works')
            request.session['it']=0
            marcaId=request.POST.get('select','')
            p=encuesta.marca_set.get(pk=marcaId)
            p.precioE=p.precio
            p.save()
            return HttpResponseRedirect(reverse('homepage'))
    # else:
    #     print('works')
    #     for marca in encuesta.marca_set.iterator():
    #         p=encuesta.marca_set
    #         p.precioE=p.get(marca.id).precio
    #         p.save()
    #     return render(request, 'home/preguntas.html',{'encuesta':encuesta})
    return render(request, 'home/preguntas.html',{'encuesta':encuesta})

def resultados(request,pk):
    encuesta=Encuesta.objects.get(pk=pk)
    return render(request,'home/resultados.html',{'encuesta':encuesta})

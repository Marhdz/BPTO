from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import EncuestaForm, MarcaForm
from django.utils import timezone
from django.views.generic import CreateView
from .models import Encuesta, Marca
from django.urls import reverse
from django.views import generic
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

def r(request):
	encuesta = Encuesta.objects.values()#obtenemos nuestros datos
	return render(request,'resultados.html',{'datos':encuesta})

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

def pregunta(request, pk):
    encuesta=Encuesta.objects.get(pk=pk)
    if request.method == 'POST':
        if request.session['it']<=encuesta.numIteraciones:
            request.session['it']+=1
            marcaId=request.POST.get('select','')
            marca=Marca.objects.get(pk=marcaId)
            # marca.precioE=5
            # print('check')
            # print(marca.precioE)
            # marca.precioE.save()

        else:
            request.session['it']=0
            return HttpResponseRedirect(reverse('homepage'))
        # if request.POST.get("{{marca.id}}")
    return render(request, 'home/preguntas.html',{'encuesta':encuesta})

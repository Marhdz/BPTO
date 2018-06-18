from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Encuesta, Marca, Opciones

class EncuestaForm(ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre', 'incremento', 'numIteraciones','categoria']

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'imagen', 'precio']

class OpcionesForm(ModelForm):
    class Meta:
        model = Opciones
        fields = ['nIteracion']

MarcaFormSet= inlineformset_factory(Encuesta,Marca, fields=['nombre','precio', 'imagen'])
OpcionesFormSet= inlineformset_factory(Marca, Opciones, fields=['nIteracion'])

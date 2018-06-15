from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Encuesta, Marca

class EncuestaForm(ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre', 'incremento', 'numIteraciones','categoria']

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre', 'imagen', 'precio']

MarcaFormSet= inlineformset_factory(Encuesta,Marca, fields=['nombre','precio', 'imagen'])

from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Encuesta, Marca

class EncuestaForm(ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre', 'incremento', 'numIteraciones','categoria']

MarcaFormSet= inlineformset_factory(Encuesta,Marca, fields=['nombre','precio','imagen'])

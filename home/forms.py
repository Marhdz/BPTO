from django.db import models
from django import forms
from .models import Encuesta

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre', 'incremento', 'numIteraciones','categoria','marca']

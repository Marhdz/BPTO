from django.contrib import admin
from home.models import Encuesta, Marca
from django import forms


class MarcasInline(admin.StackedInline):
    model = Marca
    extra = 2


class EncuestaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nombre','categoria','incremento', 'numIteraciones','date']}),
        #('Date information', {'fields': ['date']}),
    ]
    inlines = [MarcasInline]
    list_display = ('nombre', 'date')
admin.site.register(Encuesta, EncuestaAdmin)

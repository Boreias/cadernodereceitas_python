from django import forms
from django.core.mail.message import EmailMessage

from .models import TipoReceita


class ReceitaForm(forms.Form):
    titulo = forms.CharField(label='Titulo', max_length=100)
    TIPO = TipoReceita.objects.values_list('id', 'descricao')
    tipo = forms.ChoiceField(choices=TIPO)
    ingredientes = forms.Textarea()
    preparo = forms.Textarea()

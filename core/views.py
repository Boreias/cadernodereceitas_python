from django.views.generic import ListView, FormView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

#from .forms import ReceitaForm


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class ReceitaView(TemplateView):
    template_name = 'receita.html'


class CadastroReceitaView(TemplateView):
    template_name = 'cadastro-receita.html'


class ListaReceitasView(TemplateView):
    pass
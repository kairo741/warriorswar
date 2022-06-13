from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Cidade, Pessoa
from braces.views import GroupRequiredMixin


# Create your views here.


class Index(TemplateView):
    template_name = 'pages/index.html'


class CidadeCreate(GroupRequiredMixin, CreateView):
    group_required = u'Administrador'
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'register/form.html'
    success_url = reverse_lazy('index')


class PessoaCreate(CreateView, UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'idade', 'email', 'cidade']
    template_name = 'register/form.html'
    success_url = reverse_lazy('index')


class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'register/form.html'
    success_url = reverse_lazy('index')


class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'idade', 'email', 'cidade']
    template_name = 'register/form.html'
    success_url = reverse_lazy('index')

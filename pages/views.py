from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Cidade, Pessoa, Sprite
from braces.views import GroupRequiredMixin
from django.contrib.auth.models import User


# Create your views here.


class Index(TemplateView):
    template_name = 'pages/index/index-content.html'


class SpriteCreate(GroupRequiredMixin, CreateView):
    group_required = u'Administrador'
    model = Sprite
    fields = ['name', 'base64', 'type']
    template_name = 'pages/register/register-element.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.user = self.request.user
        url = super().form_valid(form)
        self.object.save()
        return url


class PessoaCreate(CreateView, UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'idade', 'email', 'cidade']
    template_name = 'register/register_account.html'
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


class UserCreate(CreateView):
    model = User
    fields = ["first_name", "last_name", "email", "password"]
    template_name = 'register/register_account.html'
    success_url = reverse_lazy('index')

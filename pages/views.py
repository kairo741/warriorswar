from braces.views import GroupRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Sprite, Element, Equipment, Spell, Effect, Warrior

# Create your views here.

adm_group = u'Administrador'


class Index(TemplateView):
    template_name = 'pages/index/index-content.html'


# ----------------- WARRIOR -----------------
class WarriorCreate(CreateView):
    model = Warrior
    fields = ['name']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-warrior')

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        self.object.save()
        return url


class WarriorUpdate(UpdateView):
    model = Warrior
    fields = ['name']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-warrior')

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        self.object.save()
        return url


class WarriorList(ListView):
    model = Warrior
    template_name = 'pages/list/warrior-list.html'


class WarriorDelete(DeleteView):
    model = Warrior
    success_url = reverse_lazy('list-warrior')


# ----------------- SPRITE -----------------
class SpriteCreate(GroupRequiredMixin, CreateView):
    group_required = adm_group
    model = Sprite
    fields = ['name', 'base64', 'type']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-sprite')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.user = self.request.user
        url = super().form_valid(form)
        self.object.save()
        return url


class SpriteUpdate(GroupRequiredMixin, UpdateView):
    group_required = adm_group
    model = Sprite
    fields = ['name', 'base64', 'type']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-sprite')

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        self.object.save()
        return url


class SpriteList(ListView):
    model = Sprite
    template_name = 'pages/list/sprite-list.html'


class SpriteDelete(DeleteView):
    model = Sprite
    success_url = reverse_lazy('list-sprite')


# ----------------- ELEMENT -----------------
class ElementCreate(GroupRequiredMixin, CreateView):
    group_required = adm_group
    model = Element
    fields = ['name']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-element')


class ElementUpdate(GroupRequiredMixin, UpdateView):
    group_required = adm_group
    model = Element
    fields = ['name']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-element')


class ElementList(ListView):
    model = Element
    template_name = 'pages/list/element-list.html'


class ElementDelete(DeleteView):
    model = Element
    success_url = reverse_lazy('list-element')


# ----------------- EQUIPMENT -----------------
class EquipmentCreate(GroupRequiredMixin, CreateView):
    group_required = adm_group
    model = Equipment
    fields = ['name', 'type', 'rarity', 'color']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-equipment')


class EquipmentUpdate(GroupRequiredMixin, UpdateView):
    group_required = adm_group
    model = Equipment
    fields = ['name', 'type', 'rarity', 'color']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-equipment')


class EquipmentList(ListView):
    model = Equipment
    template_name = 'pages/list/equipment-list.html'


class EquipmentDelete(DeleteView):
    model = Equipment
    success_url = reverse_lazy('list-equipment')


# ----------------- SPELL -----------------
class SpellCreate(CreateView):
    # group_required = adm_group
    model = Spell
    fields = ['name', 'mana_cost']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-spell')

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        self.object.save()
        return url


class SpellUpdate(UpdateView):
    # group_required = adm_group
    model = Spell
    fields = ['name', 'mana_cost']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-spell')

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        self.object.save()
        return url


class SpellList(ListView):
    model = Spell
    template_name = 'pages/list/spell-list.html'


class SpellDelete(DeleteView):
    model = Spell
    success_url = reverse_lazy('list-spell')


# ----------------- EFFECT -----------------
class EffectCreate(GroupRequiredMixin, CreateView):
    group_required = adm_group
    model = Effect
    fields = ['name']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-effect')


class EffectUpdate(GroupRequiredMixin, UpdateView):
    group_required = adm_group
    model = Effect
    fields = ['name']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-effect')


class EffectList(ListView):
    model = Effect
    template_name = 'pages/list/effect-list.html'


class EffectDelete(DeleteView):
    model = Effect
    success_url = reverse_lazy('list-effect')


class UserCreate(CreateView):
    model = User
    fields = ["first_name", "last_name", "email", "password"]
    template_name = 'register/register_account.html'
    success_url = reverse_lazy('index')

# class PessoaCreate(CreateView, UpdateView):
#     model = Pessoa
#     fields = ['nome_completo', 'idade', 'email', 'cidade']
#     template_name = 'register/register_account.html'
#     success_url = reverse_lazy('index')
#
#
# class CidadeUpdate(UpdateView):
#     model = Cidade
#     fields = ['nome', 'estado']
#     template_name = 'register/form.html'
#     success_url = reverse_lazy('index')
#
#
# class PessoaUpdate(UpdateView):
#     model = Pessoa
#     fields = ['nome_completo', 'idade', 'email', 'cidade']
#     template_name = 'register/form.html'
#     success_url = reverse_lazy('index')

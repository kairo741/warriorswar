from braces.views import GroupRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Sprite, Element, Equipment, Spell, Effect, Warrior
from .templatetags.auth_extras import has_group

# Create your views here.

adm_group = u'admins'
normal_user_group = u'summoners'


class Index(TemplateView):
    template_name = 'pages/index/index-content.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = context['view'].request.user
        all_warriors = Warrior.objects.all().count()
        context['all_warriors'] = all_warriors
        context['all_users'] = User.objects.all().count()
        if user.is_authenticated:
            user_warriors = Warrior.objects.filter(user=user).count()
            context['user_warriors'] = user_warriors
            context['percent_warriors'] = f'{(user_warriors / all_warriors) * 100:.2f}'

        return context


# ----------------- WARRIOR -----------------
class WarriorCreate(GroupRequiredMixin, CreateView):
    group_required = normal_user_group
    model = Warrior
    fields = ['name']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-warrior')

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        self.object.save()
        return url


class WarriorUpdate(GroupRequiredMixin, UpdateView):
    group_required = normal_user_group
    model = Warrior
    fields = ['name']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-warrior')

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        self.object.save()
        return url

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Warrior, pk=self.kwargs['pk'], user=self.request.user)
        return self.object


class WarriorList(GroupRequiredMixin, ListView):
    group_required = normal_user_group
    model = Warrior
    template_name = 'pages/list/warrior-list.html'

    def get_queryset(self):
        if not has_group(self.request.user, adm_group):
            self.object_list = Warrior.objects.filter(user=self.request.user)
            return self.object_list
        else:
            return Warrior.objects.all()


class WarriorDelete(DeleteView):
    model = Warrior
    success_url = reverse_lazy('list-warrior')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Warrior, pk=self.kwargs['pk'], user=self.request.user)
        return self.object


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
class SpellCreate(GroupRequiredMixin, CreateView):
    group_required = normal_user_group
    model = Spell
    fields = ['name', 'mana_cost']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-spell')

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        self.object.save()
        return url


class SpellUpdate(GroupRequiredMixin, UpdateView):
    group_required = normal_user_group
    model = Spell
    fields = ['name', 'mana_cost']
    template_name = 'pages/register/base-register.html'
    success_url = reverse_lazy('list-spell')

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        self.object.save()
        return url

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Spell, pk=self.kwargs['pk'], user=self.request.user)
        return self.object


class SpellList(GroupRequiredMixin, ListView):
    group_required = normal_user_group
    model = Spell
    template_name = 'pages/list/spell-list.html'

    def get_queryset(self):
        if not has_group(self.request.user, adm_group):
            self.object_list = Spell.objects.filter(user=self.request.user)
            return self.object_list
        else:
            return Warrior.objects.all()


class SpellDelete(DeleteView):
    model = Spell
    success_url = reverse_lazy('list-spell')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Spell, pk=self.kwargs['pk'], user=self.request.user)
        return self.object


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


# class UserCreate(CreateView):
#     model = User
#     fields = ["first_name", "last_name", "email", "password"]
#     template_name = 'register/register_account.html'
#     success_url = reverse_lazy('index')


# ----------------- HANDLERS -----------------
def handler404(request, exception):
    return render(request, 'pages/error-handler/404.html', {})
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

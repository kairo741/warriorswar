from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ESTADOS_CHOICES = [
    ('PR', 'Paraná'),
    ('SP', 'São Paulo'),
    ('RJ', 'Rio de Janeiro'),
    ('MT', 'Mato Grosso'),
    ('SC', 'Santa Catarina'),
    ('AC', 'Acre'),
]


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.CharField(max_length=2, choices=ESTADOS_CHOICES, default=ESTADOS_CHOICES[2])

    def __str__(self):
        return f'{self.nome} - {self.estado}'


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=50, verbose_name="Nome", help_text="Digite seu nome completo")
    idade = models.DateField(verbose_name='Data de nascimento')
    email = models.EmailField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome_completo


class Sprite(models.Model):
    name = models.CharField(max_length=255)
    base64 = models.CharField(max_length=5000)
    type = models.CharField(max_length=50)

    active = models.BooleanField(default=True)
    registered_in = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Element(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Effect(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.type} {self.name}'


class Warrior(models.Model):
    name = models.CharField(max_length=255)
    # sprite = models.ManyToManyField(choices=Sprite)

    active = models.BooleanField(default=True)
    registered_in = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Spell(models.Model):
    name = models.CharField(max_length=255)
    mana_cost = models.FloatField()

    active = models.BooleanField(default=True)
    registered_in = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Attributes(models.Model):
    health_points = models.FloatField()
    mana = models.FloatField()
    strength = models.FloatField()
    xp = models.FloatField()
    armor = models.FloatField()
    crit_rate = models.FloatField()

    active = models.BooleanField(default=True)
    registered_in = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return '{:.2f} - Atributos: {:.2f} | {:.2f} | {:.2f} | {:.2f} | {:.2f} | {:.2f}' \
            .format(self.pk, self.health_points, self.mana, self.strength, self.xp, self.armor, self.crit_rate)

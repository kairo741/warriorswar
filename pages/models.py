from django.db import models

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

from django.db import models

from forms.choices import Seniority

from datetime import datetime


class BaseModel(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True


class Programmer(BaseModel):
    first_name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100, help_text='Deve terminar com @dominio.com')
    birth_date = models.DateField('Data de nascimento')
    seniority = models.CharField('Senioridade', max_length=10, choices=Seniority.choices)

    def age(self):
        return self.birth_date - datetime.now()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Programador'
        verbose_name_plural = 'Programadores'

    # TODO Criar função que retorne a idade do programador
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

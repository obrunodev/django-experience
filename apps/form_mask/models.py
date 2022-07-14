from django.db import models


class Person(models.Model):
    name = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=20)
    birth_date = models.CharField('Data de nascimento', max_length=10)
    phone = models.CharField('Telefone', max_length=20)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

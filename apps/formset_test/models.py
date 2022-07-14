from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        abstract = True


class Customer(BaseModel):
    name = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=20)
    birth_date = models.DateField('Data de nascimento')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.name


class Phone(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    number = models.CharField('Número de telefone', max_length=20)
    
    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'
    
    def __str__(self):
        return self.number

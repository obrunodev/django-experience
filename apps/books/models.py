from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True


class Book(BaseModel):
    title = models.CharField('Título', max_length=100)
    author = models.CharField('Autor', max_length=100)
    pages = models.IntegerField('Páginas')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

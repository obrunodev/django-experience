from django.contrib import admin

from formset_test.models import Customer
from formset_test.models import Phone


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf')
    # list_display_links = ('title', 'author')
    # list_filter = ('author',)
    list_per_page = 20
    list_max_show_all = 100
    empty_value_display = 'Vazio'
    search_fields = ['name', 'cpf']

    # QUAIS CAMPOS DEVE APARECER/REMOVER DA TELA DE EDIÇÃO
    # fields = (('first_name', 'last_name'), 'seniority')
    # exclude = ('first_name', 'last_name')


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

from forms.models import Programmer

@admin.register(Programmer)
class ProgrammerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'seniority')
    list_display_links = ('full_name', 'email')
    list_filter = ('seniority',)
    list_per_page = 20
    list_max_show_all = 100
    empty_value_display = 'Vazio'
    search_fields = ['first_name', 'last_name']

    # QUAIS CAMPOS DEVE APARECER/REMOVER DA TELA DE EDIÇÃO
    # fields = (('first_name', 'last_name'), 'seniority')
    # exclude = ('first_name', 'last_name')

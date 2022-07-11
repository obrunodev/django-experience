from django.core.exceptions import ValidationError
from django import forms

from books.models import Book


class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'pages']
        error_messages = {
            'title': {
                'required': 'Este campo é obrigatório.',
                'max_length': 'Este campo não pode ter mais de 100 caracteres.'
            }
        }
        # widgets = {
        #     'first_name': forms.TextInput(attrs={
        #         'class': 'form-control'
        #     })
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['pages'].widget.attrs.update({'class': 'form-control'})
    
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('title') == "":
            name_empty_error = ValidationError(
                'Este campo precisa estar preenchido',
                code='Invalid'
            )
            raise ValidationError({'title': name_empty_error})


BookFormSet = forms.modelformset_factory(Book, fields=('title', 'author', 'pages'), extra=2)

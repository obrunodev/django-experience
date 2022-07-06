from django.core.exceptions import ValidationError
from django import forms

from forms.models import Programmer


class ProgrammerForm(forms.ModelForm):

    class Meta:
        model = Programmer
        fields = ['first_name', 'last_name', 'email', 'birth_date', 'seniority']
        error_messages = {
            'first_name': {
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
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})

        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})

        self.fields['birth_date'].widget.attrs.update({
            'class': 'form-control',
            'data-toggle': 'datepicker',
        })

        self.fields['seniority'].widget.attrs.update({'class': 'form-control'})

        self.fields['email'].widget.attrs.update({
            'placeholder': "Digite seu e-mail aqui.",
            'class': 'form-control',
        })
    
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('first_name') == "":
            name_empty_error = ValidationError(
                'Este campo precisa estar preenchido',
                code='Invalid'
            )
            raise ValidationError({'first_name': name_empty_error})
from dataclasses import field
from django import forms

from form_mask.models import Person


class PersonForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = '__all__'
    
    def __init__(self,*args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control mask-cpf'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control mask-phone'})
        self.fields['birth_date'].widget.attrs.update({'class': 'form-control mask-date'})

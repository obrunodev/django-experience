from django import forms
from django.forms import inlineformset_factory

from formset_test.models import Customer
from formset_test.models import Phone


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
    
    def __init__(self,*args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control mask-cpf'})
        self.fields['birth_date'].widget.attrs.update({'class': 'form-control mask-date'})


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'


PhoneInlineFormset = inlineformset_factory(Customer, Phone, form=PhoneForm, min_num=1, max_num=10, extra=0)

from django import forms
from django.forms import inlineformset_factory

from formset_test.models import Customer
from formset_test.models import Phone


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'


PhoneInlineFormset = inlineformset_factory(Customer, Phone, form=PhoneForm, extra=3)

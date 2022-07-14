from django import forms

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

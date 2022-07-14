from django.contrib import admin

from formset_test.models import Customer
from formset_test.models import Phone


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from formset_test.forms import CustomerForm
from formset_test.forms import PhoneInlineFormset
from formset_test.models import Customer


def customers_list(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'formset_test/pages/customers_list.html', context)


def customers_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo cliente cadastrado!')
            return redirect('formset_test:customers_list')
        context = {'form': form}

    if request.method == 'GET':
        form = CustomerForm()
        context = {'form': form}

    return render(request, 'formset_test/pages/customers_create.html', context)


def customers_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        try:
            customer.delete()
            messages.success(request, f'Cliente "{customer.name}" foi removido.')
        except Exception as e:
            messages.error(request, 'Algo deu errado, tente novamente!')
    
    return redirect('formset_test:customers_list')


def phone_create(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    
    if request.method == 'POST':
        pass
    
    if request.method == 'GET':
        formset = PhoneInlineFormset()
        context = {'formset': formset,
                   'customer': customer}
    
    return render(request, 'formset_test/pages/phone_create.html', context)

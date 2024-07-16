from apps.users.forms import UserForm
from django.contrib import messages
from django.shortcuts import redirect, render


def signup(request):
    if request.method == 'GET':
        form = UserForm()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            new_user = form.save()
            new_user.set_password(password)
            new_user.save()
            messages.success(request, 'User has been created!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'users/signup.html', context)

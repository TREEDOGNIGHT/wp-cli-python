from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import render, redirect

from apps.users.forms import UserForm, SearchUserForm, NewUserForm
from apps.users.models import User


def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        form = SearchUserForm()

    
    if request.method == 'POST':
        form = SearchUserForm(request.POST)

        if form.is_valid():
            search = form.cleaned_data.get('search')
            users = User.objects.filter(
                Q(user_login__icontains=search)
                | Q(user_display_name__icontains=search)
            )



    return render(
        request,
        'users/users.html',
        {'users': users, 'form': form}
    )


def add_users(request):
    if request.method == 'GET':
        form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('users')

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )

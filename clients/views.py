from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/welcome')
    return render(request, 'log_in.html', {})


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = User.objects.create_user(username=username,
                                        password=password)
        user.save()
        return redirect('/log_in/')
    return render(request, 'sign_up.html', {})


def welcome(request):
    return render(request, 'welcome.html', {})

from django.shortcuts import render, redirect


from django.shortcuts import render, redirect
from .forms import RegisterForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, f'user has been created successfully')
    return render(request, 'users_register.html')

def login_view(request):
    form = UserLoginForm()
    username = request.POST.get('')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, f'user {user.username} has been logged in')
            return redirect('home')
        else:
            messages.add_message(request, messages.WARNING, 'WRONG CREDENTIALS')
    return render(request, 'users_login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
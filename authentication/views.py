from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

def register(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/register')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe esse usuário cadastrado')
            return redirect('/auth/register')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            message.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')
            return redirect('/auth/login')
        except:
            message.add_message(request, constants.ERROR, 'Erro interno no servidor')
            return redirect('/auth/register')

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if not user:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos!')
            return redirect('/auth/login')
        else:
            auth.login(request, user)
            return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/auth/login')

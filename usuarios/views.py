# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import LoginForm, Perfil, UserForm, UsuarioForm
from .models import Perfil
from django.contrib.auth.models import User
from .usaurio import fondear_cuenta
from decimal import Decimal

def login_user(request):
    if request.user.is_authenticated():
        return redirect("venta:dashboard")
    else:
        if request.method == "POST":
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    print "si se logeo"
                    return redirect("venta:dashboard")
                else:
                    form = LoginForm()
                    return render(request, 'usuarios/login.html', {'form': form})
        else:
            form = LoginForm()
        
            return render(request, 'usuarios/login.html', {'form': form})
            
def logout_user(request):
    logout(request)
    return redirect('/')

def guardar_usuario(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        usuario_form = UsuarioForm(request.POST)
        if user_form.is_valid() and usuario_form.is_valid():
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            user = User.objects.create_user(username,email,password)
            user.first_name =  user_form.cleaned_data['first_name']

            usuario = usuario_form.save(commit=False)
            user.save()                        
            usuario.usuario = user
            usuario.save()
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect("venta:dashboard")

    
    elif request.method == "GET":
        user_form = UserForm()
        form_usuario = UsuarioForm()
        return render(request, "usuarios/crear_usuario.html", {'user_form': user_form, 'usuario_form': form_usuario})

def fondear_cuenta_perfil(request):
    if request.method == "POST":
        monto = Decimal(request.POST.get('monto', 0))
        fondear_cuenta(request,monto)
        messages.success(request, 'Se fondeo correctamente la cuenta')
        return redirect("venta:dashboard")
    if request.method ==  "GET":
        return render(request, 'usuarios/fondear_cuenta.html')

from django.shortcuts import render, redirect
from .forms import RegistrationFormUser, LoginFormUser as LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.  

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 print("Inicio de sesión exitoso")
#                 login(request, user)
#                 messages.success(request, 'Sesión iniciada exitosamente')
#                 return redirect('dashboard/index.html')
#             else:
#                 print("Usuario o contraseñ incorrectos")
#                 messages.error(request, 'Usuario o contraseña incorrectos')
#         else:
#             messages.error(request, 'Error al iniciar sesión')
#     else:
#         form = LoginForm()
#     return render(request, 'login/index.html', {'form': form, 'header_type': 'login'})

def index(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("Inicio de sesión exitoso")
                login(request, user)
                messages.success(request, 'Sesión iniciada exitosamente')
                return render(request, 'dashboard', {'header_type': 'dashboard'})
            else:
                print("Usuario o contraseñ incorrectos")
                messages.error(request, 'Usuario o contraseña incorrectos')
        else:
            messages.error(request, 'Error al iniciar sesión')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form, 'header_type': 'index'})

def dashboard(request):
    return render(request, 'dashboard/index.html', {'header_type': 'index'})

def register(request):
    if request.method == 'POST':
        form = RegistrationFormUser(request.POST)
        if form.is_valid():
            form.save() # Guardar el usuario en la base de datos
            messages.success(request, 'Usuario registrado exitosamente')
            return render(request, 'dahsboard/index.html', {'header_type': 'dashboard'})
        else:
            messages.error(request, 'Error al registrar el usuario')
    else:
        form = RegistrationFormUser()
    return render(request, 'register/index.html', {'form': form, 'header_type': 'register'})

# librerias del CRUD
from django.shortcuts import render
from principal.models import * #con opcion de quitar pricipal
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Habilitamos los mensajes para class-based views  
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
# Habilitamos el uso de mensajes en Django
from django.contrib import messages
# Habilitamos los formularios en Django
from django import forms 
from django.contrib.auth import authenticate,get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from .forms import *


# Create your views here.

def Login(request):
    return render (request, "login.html")
def Perfil(request):
    
    return render (request, "perfil.html")

def Home(request):
    
    return render (request, "index.html")

def Parametros (request):
   return render (request, "nav.html")

def Catalogo (request):
   return render (request, "CATALOGO/catalogo.html")
 
def Home1(request):
    
    return render (request, "pagina gym/index.html")

def quienessomos(request):
    
    return render (request, "pagina gym/quienessomos.html")

def contacto(request):
    
    return render (request, "pagina gym/contacto.html") 

from django.shortcuts import render, redirect


from django.views.generic import CreateView, TemplateView

from .models import *

from .forms import SignUpForm
from django.contrib.auth.views import LoginView
# Habilitamos los formularios en Django
from django import forms

class SignUpView(CreateView):
    model = AuthUser
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('login')




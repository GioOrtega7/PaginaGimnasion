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
    
    return render (request, "GENERAL/index.html")


def Parametros1 (request):
   return render (request, "GENERAL/index.html")  

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



 #---------------------------Cargo-----------------------------------#
 

class ListadoCargo(CreateView,ListView,SuccessMessageMixin):
    
    model = Cargo
    form = Cargo
    fields = "__all__"
    success_message ='Cargo creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal1:leercargo') # Redireccionamos a la vista principal 'leercargo'


class CargoDetalle (DetailView):
    model =Cargo


class  CargoActualizar(SuccessMessageMixin,UpdateView):
    model =  Cargo
    form = Cargo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'cargo' de nuestra Base de Datos 
    success_message = 'Cargo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar 


    def get_success_url(self):               
        return reverse('principal1:leercargo') # Redireccionamos a la vista principal1 'leercargo'
class CargoEliminar(SuccessMessageMixin, DeleteView): 
    model = Cargo
    form = Cargo
    fields = "__all__"     
 
    # Redireccionamos a la página principal1 luego de eliminar un registro 
    
    def get_success_url(self): 
        success_message = 'Cargo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal1:leercargo') # Redireccionamos a la vista principal 'leercargo'
    
#---------------------------Cargo-----------------------------------#


#---------------------------Estado-----------------------------------#

class ListadoEstado(CreateView,ListView,SuccessMessageMixin):
    model = Estado
    form = Estado
    fields = "__all__"
    success_message ='Estado creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal1:leerestado') # Redireccionamos a la vista principal 'leerestado'
        


class EstadoDetalle (DetailView):
    model =Estado


class  EstadoActualizar(SuccessMessageMixin,UpdateView):
    model =  Estado
    form = Estado
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Estado' de nuestra Base de Datos 
    success_message = 'Estado Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal1:leerestado') # Redireccionamos a la vista principal1 'leerestado'
class EstadoEliminar(SuccessMessageMixin, DeleteView): 
    model = Estado
    form = Estado
    fields = "__all__"     
 
    # Redireccionamos a la página principal1 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Estado Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal1:leerestado') # Redireccionamos a la vista principal 'leerestado'
    
#---------------------------Estado-----------------------------------#



#---------------------------Genero-----------------------------------#

class ListadoGenero(CreateView,ListView,SuccessMessageMixin):
    model = Genero
    form = Genero
    fields = "__all__"
    success_message ='Genero creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal1:leergenero') # Redireccionamos a la vista principal 'leergenero'
        


class GeneroDetalle (DetailView):
    model =Genero


class  GeneroActualizar(SuccessMessageMixin,UpdateView):
    model =  Genero
    form = Genero
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Genero' de nuestra Base de Datos 
    success_message = 'Genero Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal1:leergenero') # Redireccionamos a la vista principal1 'leergenero'
class GeneroEliminar(SuccessMessageMixin, DeleteView): 
    model = Genero
    form = Genero
    fields = "__all__"     
 
    # Redireccionamos a la página principal1 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Genero Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal1:leergenero') # Redireccionamos a la vista principal 'leergenero'
    
#---------------------------Genero-----------------------------------#

#---------------------------Ocupacion-----------------------------------#

class ListadoOcupacion(CreateView,ListView,SuccessMessageMixin):
    model = Ocupacion
    form = Ocupacion
    fields = "__all__"
    success_message ='Ocupacion creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal1:leerocupacion') # Redireccionamos a la vista principal 'leerocupacion'
        


class OcupacionDetalle (DetailView):
    model =Ocupacion


class  OcupacionActualizar(SuccessMessageMixin,UpdateView):
    model =  Ocupacion
    form = Ocupacion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Ocupacion' de nuestra Base de Datos 
    success_message = 'Ocupacion Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal1:leerocupacion') # Redireccionamos a la vista principal1 'leerocupacion'
class OcupacionEliminar(SuccessMessageMixin, DeleteView): 
    model = Ocupacion
    form = Ocupacion
    fields = "__all__"     
 
    # Redireccionamos a la página principal1 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Ocupacion Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal1:leerocupacion') # Redireccionamos a la vista principal 'leerocupacion'
    
#---------------------------Ocupacion-----------------------------------#



#---------------------------Persona-----------------------------------#

class ListadoPersona(CreateView,ListView,SuccessMessageMixin):
    model = Persona
    form = Persona
    fields = "__all__"
    success_message ='Persona creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal1:leerpersona') # Redireccionamos a la vista principal 'leerpersona'
        


class PersonaDetalle (DetailView):
    model =Persona


class  PersonaActualizar(SuccessMessageMixin,UpdateView):
    model =  Persona
    form = Persona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Persona' de nuestra Base de Datos 
    success_message = 'Persona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal1:leerpersona') # Redireccionamos a la vista principal1 'leerpersona'
class PersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Persona
    form = Persona
    fields = "__all__"     
 
    # Redireccionamos a la página principal1 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Persona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal1:leerpersona') # Redireccionamos a la vista principal 'leerpersona'
    
#---------------------------Persona-----------------------------------#


#---------------------------Tipodocumento-----------------------------------#

class ListadoTipodocumento(CreateView,ListView,SuccessMessageMixin):
    model = Tipodocumento
    form = Tipodocumento
    fields = "__all__"
    success_message ='Tipodocumento creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal1:leertipodocumento') # Redireccionamos a la vista principal 'leertipodocumento'
        


class TipodocumentoDetalle (DetailView):
    model =Tipodocumento


class  TipodocumentoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipodocumento
    form = Tipodocumento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Tipodocumento' de nuestra Base de Datos 
    success_message = 'Tipodocumento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal1:leertipodocumento') # Redireccionamos a la vista principal1 'leertipodocumento'
class TipodocumentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipodocumento
    form = Tipodocumento
    fields = "__all__"     
 
    # Redireccionamos a la página principal1 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Tipodocumento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal1:leertipodocumento') # Redireccionamos a la vista principal 'leertipodocumento'
    
#---------------------------Tipodocumento-----------------------------------#



#---------------------------Tipopersona-----------------------------------#

class ListadoTipopersona(CreateView,ListView,SuccessMessageMixin):
    model = Tipopersona
    form = Tipopersona
    fields = "__all__"
    success_message ='Tipopersona creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal1:leertipopersona') # Redireccionamos a la vista principal 'leertipersona'
        


class TipopersonaDetalle (DetailView):
    model =Tipopersona


class  TipopersonaActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipopersona
    form = Tipopersona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Tipopersona' de nuestra Base de Datos 
    success_message = 'Tipopersona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal1:leertipopersona') # Redireccionamos a la vista principal1 'leertipersona'
class TipopersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipopersona
    form = Tipopersona
    fields = "__all__"     
 
    # Redireccionamos a la página principal1 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Tipopersona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal1:leertipopersona') # Redireccionamos a la vista principal 'leertipersona'
    
#---------------------------Tipopersona-----------------------------------#

#---------------------------Historia-----------------------------------#

class ListadoHistoria(CreateView,ListView,SuccessMessageMixin):
    model = Historia
    form = Historia
    fields = "__all__"
    success_message ='Historia creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal1:leerhistoria') # Redireccionamos a la vista principal 'leerhistoria'
        


class HistoriaDetalle (DetailView):
    model =Historia


class  HistoriaActualizar(SuccessMessageMixin,UpdateView):
    model =  Historia
    form = Historia
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Historia' de nuestra Base de Datos 
    success_message = 'Historia Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal1:leerhistoria') # Redireccionamos a la vista principal1 'leerhistoria'
class HistoriaEliminar(SuccessMessageMixin, DeleteView): 
    model = Historia
    form = Historia
    fields = "__all__"     
 
    # Redireccionamos a la página principal1 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Historia Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal1:leerhistoria') # Redireccionamos a la vista principal 'leerhistoria'
    
#---------------------------Historia-----------------------------------#



#---------------------------Usuario-----------------------------------#

class ListadoUsuario(CreateView,ListView,SuccessMessageMixin):
    model = Usuario
    form = Usuario
    fields = "__all__"
    success_message ='Usuario creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal1:leerusuario') # Redireccionamos a la vista principal 'leerusuario'
        


class UsuarioDetalle (DetailView):
    model =Usuario


class  UsuarioActualizar(SuccessMessageMixin,UpdateView):
    model =  Usuario
    form = Usuario
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Usuario' de nuestra Base de Datos 
    success_message = 'Usuario Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal1:leerusuario') # Redireccionamos a la vista principal1 'leerusuario'
class UsuarioEliminar(SuccessMessageMixin, DeleteView): 
    model = Usuario
    form = Usuario
    fields = "__all__"     
 
    # Redireccionamos a la página principal1 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Usuario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal1:leerusuario') # Redireccionamos a la vista principal 'leerusuario'
    
#---------------------------Usuario-----------------------------------#
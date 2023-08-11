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


def Parametros2 (request):
   return render (request, "CRONOGRAMA/index.html")  

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





#---------------------------Cita-----------------------------------#

class ListadoCita(CreateView,ListView,SuccessMessageMixin):
    model = Cita
    form = Cita
    fields = "__all__"
    success_message ='Cita creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal2:leercita') # Redireccionamos a la vista principal2 'leercita'
        


class CitaDetalle (DetailView):
    model =Cita


class  CitaActualizar(SuccessMessageMixin,UpdateView):
    model =  Cita
    form = Cita
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'cita' de nuestra Base de Datos 
    success_message = 'Cita Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal2:leercita') # Redireccionamos a la vista principal2 'leercita'
class CitaEliminar(SuccessMessageMixin, DeleteView): 
    model = Cita
    form = Cita
    fields = "__all__"     
 
    # Redireccionamos a la página principal2 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Cita Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal2:leercita') # Redireccionamos a la vista principal2 'leercita'
    
#---------------------------Cita-----------------------------------#



#---------------------------dia-----------------------------------#

class ListadoDia(CreateView,ListView,SuccessMessageMixin):
    model = Dia
    form = Dia
    fields = "__all__"
    success_message ='dia creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal2:leerdia') # Redireccionamos a la vista principal2 'leerDia'
        


class DiaDetalle (DetailView):
    model =Dia


class  DiaActualizar(SuccessMessageMixin,UpdateView):
    model =  Dia
    form = Dia
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Dia' de nuestra Base de Datos 
    success_message = 'Dia Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal2:leerdia') # Redireccionamos a la vista principal2 'leerDia'
class DiaEliminar(SuccessMessageMixin, DeleteView): 
    model = Dia
    form = Dia
    fields = "__all__"     
 
    # Redireccionamos a la página principal2 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Dia Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal2:leerdia') # Redireccionamos a la vista principal2 'leerDia'
    
#---------------------------dia-----------------------------------#





#---------------------------Enfoque-----------------------------------#

class ListadoEnfoque(CreateView,ListView,SuccessMessageMixin):
    model = Enfoque
    form = Enfoque
    fields = "__all__"
    success_message ='Enfoque creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal2:leerenfoque') # Redireccionamos a la vista principal2 'leerenfoque'
        


class EnfoqueDetalle (DetailView):
    model =Enfoque


class  EnfoqueActualizar(SuccessMessageMixin,UpdateView):
    model =  Enfoque
    form = Enfoque
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Enfoque' de nuestra Base de Datos 
    success_message = 'Enfoque Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal2:leerenfoque') # Redireccionamos a la vista principal2 'leerenfoque'
class EnfoqueEliminar(SuccessMessageMixin, DeleteView): 
    model = Enfoque
    form = Enfoque
    fields = "__all__"     
 
    # Redireccionamos a la página principal2 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Enfoque Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal2:leerenfoque') # Redireccionamos a la vista principal2 'leerenfoque'
    
#---------------------------Enfoque-----------------------------------#







#---------------------------Evolucion-----------------------------------#

class ListadoEvolucion(CreateView,ListView,SuccessMessageMixin):
    model = Evolucion
    form = Evolucion
    fields = "__all__"
    success_message ='Evolucion creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal2:leerevolucion') # Redireccionamos a la vista principal2 'leerevolucion'
        


class EvolucionDetalle (DetailView):
    model =Evolucion


class  EvolucionActualizar(SuccessMessageMixin,UpdateView):
    model =  Evolucion
    form = Evolucion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Evolucion' de nuestra Base de Datos 
    success_message = 'Evolucion Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal2:leerevolucion') # Redireccionamos a la vista principal2 'leerevolucion'
class EvolucionEliminar(SuccessMessageMixin, DeleteView): 
    model = Evolucion
    form = Evolucion
    fields = "__all__"     
 
    # Redireccionamos a la página principal2 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Evolucion Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal2:leerevolucion') # Redireccionamos a la vista principal2 'leerevolucion'
    
#---------------------------Evolucion-----------------------------------#







#---------------------------Historia-----------------------------------#

class ListadoHistoria(CreateView,ListView,SuccessMessageMixin):
    model = Historia
    form = Historia
    fields = "__all__"
    success_message ='Historia creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal2:leerhistoria') # Redireccionamos a la vista principal2 'leerhistoria'
        


class HistoriaDetalle (DetailView):
    model =Historia


class  HistoriaActualizar(SuccessMessageMixin,UpdateView):
    model =  Historia
    form = Historia
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Historia' de nuestra Base de Datos 
    success_message = 'Historia Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal2:leerhistoria') # Redireccionamos a la vista principal2 'leerhistoria'
class HistoriaEliminar(SuccessMessageMixin, DeleteView): 
    model = Historia
    form = Historia
    fields = "__all__"     
 
    # Redireccionamos a la página principal2 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Historia Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal2:leerhistoria') # Redireccionamos a la vista principal2 'leerhistoria'
    
#---------------------------Historia-----------------------------------#



#---------------------------Horario-----------------------------------#

class ListadoHorario(CreateView,ListView,SuccessMessageMixin):
    model = Horario
    form = Horario
    fields = "__all__"
    success_message ='Horario creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal2:leerhorario') # Redireccionamos a la vista principal2 'leerhorario'
        


class HorarioDetalle (DetailView):
    model =Horario


class  HorarioActualizar(SuccessMessageMixin,UpdateView):
    model =  Horario
    form = Horario
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Horario' de nuestra Base de Datos 
    success_message = 'Horario Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal2:leerhorario') # Redireccionamos a la vista principal2 'leerhorario'
class HorarioEliminar(SuccessMessageMixin, DeleteView): 
    model = Horario
    form = Horario
    fields = "__all__"     
 
    # Redireccionamos a la página principal2 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Horario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal2:leerhorario') # Redireccionamos a la vista principal2 'leerhorario'
    
#---------------------------Horario-----------------------------------#









#---------------------------Plan-----------------------------------#

class ListadoPlan(CreateView,ListView,SuccessMessageMixin):
    model = Plan
    form = Plan
    fields = "__all__"
    success_message ='Plan creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal2:leerplan') # Redireccionamos a la vista principal2 'leerplan'
        


class PlanDetalle (DetailView):
    model =Plan


class  PlanActualizar(SuccessMessageMixin,UpdateView):
    model =  Plan
    form = Plan
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Plan' de nuestra Base de Datos 
    success_message = 'Plan Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 

    def get_success_url(self):               
        return reverse('principal2:leerplan') # Redireccionamos a la vista principal2 'leerplan'
    

class PlanEliminar(SuccessMessageMixin, DeleteView): 
    model = Plan
    form = Plan
    fields = "__all__"     
 
    # Redireccionamos a la página principal2 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Plan Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal2:leerplan') # Redireccionamos a la vista principal2 'leerplan'
    
#---------------------------Plan-----------------------------------#





#---------------------------Tipoplan-----------------------------------#

class ListadoTipoplan(CreateView,ListView,SuccessMessageMixin):
    model = Tipoplan
    form = Tipoplan
    fields = "__all__"
    success_message ='Tipoplan creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal2:leertipoplan') # Redireccionamos a la vista principal2 'leertipoplan'
        


class TipoplanDetalle (DetailView):
    model =Tipoplan


class  TipoplanActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipoplan
    form = Tipoplan
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Tipoplan' de nuestra Base de Datos 
    success_message = 'Tipoplan Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal2:leertipoplan') # Redireccionamos a la vista principal2 'leertipoplan'
class TipoplanEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipoplan
    form = Tipoplan
    fields = "__all__"     
 
    # Redireccionamos a la página principal2 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Tipoplan Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal2:leertipoplan') # Redireccionamos a la vista principal2 'leertipoplan'
    
#---------------------------Tipoplan-----------------------------------#




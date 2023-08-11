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


def Parametros3 (request):
   return render (request, "PROGRAMA/index.html")  

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





#---------------------------Dieta-----------------------------------#

class ListadoDieta(CreateView,ListView,SuccessMessageMixin):
    model = Dieta
    form = Dieta
    fields = "__all__"
    success_message ='Dieta creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal3:leerdieta') # Redireccionamos a la vista principal3 'leerdieta'
        


class DietaDetalle (DetailView):
    model =Dieta


class  DietaActualizar(SuccessMessageMixin,UpdateView):
    model =  Dieta
    form = Dieta
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Dieta' de nuestra Base de Datos 
    success_message = 'Dieta Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal3:leerdieta') # Redireccionamos a la vista principal3 'leerdieta'
class DietaEliminar(SuccessMessageMixin, DeleteView): 
    model = Dieta
    form = Dieta
    fields = "__all__"     
 
    # Redireccionamos a la página principal3 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Dieta Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal3:leerdieta') # Redireccionamos a la vista principal3 'leerdieta'
    
#---------------------------Dieta-----------------------------------#



#---------------------------Ejercicio-----------------------------------#

class ListadoEjercicio(CreateView,ListView,SuccessMessageMixin):
    model = Ejercicio
    form = Ejercicio
    fields = "__all__"
    success_message ='Ejercicio creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal3:leerejercicio') # Redireccionamos a la vista principal3 'leerejercicio'
        


class EjercicioDetalle (DetailView):
    model =Ejercicio


class  EjercicioActualizar(SuccessMessageMixin,UpdateView):
    model =  Ejercicio
    form = Ejercicio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Ejercicio' de nuestra Base de Datos 
    success_message = 'Ejercicio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal3:leerejercicio') # Redireccionamos a la vista principal3 'leerejercicio'
class EjercicioEliminar(SuccessMessageMixin, DeleteView): 
    model = Ejercicio
    form = Ejercicio
    fields = "__all__"     
 
    # Redireccionamos a la página principal3 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Ejercicio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal3:leerejercicio') # Redireccionamos a la vista principal3 'leerejercicio'
    
#---------------------------Ejercicio-----------------------------------#







#---------------------------Ingrediente-----------------------------------#

class ListadoIngrediente(CreateView,ListView,SuccessMessageMixin):
    model = Ingrediente
    form = Ingrediente
    fields = "__all__"
    success_message ='Ingrediente creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal3:leeringrediente') # Redireccionamos a la vista principal3 'leeringrediente'
        


class IngredienteDetalle (DetailView):
    model =Ingrediente


class  IngredienteActualizar(SuccessMessageMixin,UpdateView):
    model =  Ingrediente
    form = Ingrediente
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Ingrediente' de nuestra Base de Datos 
    success_message = 'Ingrediente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal3:leeringrediente') # Redireccionamos a la vista principal3 'leeringrediente'
class IngredienteEliminar(SuccessMessageMixin, DeleteView): 
    model = Ingrediente
    form = Ingrediente
    fields = "__all__"     
 
    # Redireccionamos a la página principal3 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Ingrediente Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal3:leeringrediente') # Redireccionamos a la vista principal3 'leeringrediente'
    
#---------------------------Ingrediente-----------------------------------#



#---------------------------Medida-----------------------------------#

class ListadoMedida(CreateView,ListView,SuccessMessageMixin):
    model = Medida
    form = Medida
    fields = "__all__"
    success_message ='Medida creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal3:leermedida') # Redireccionamos a la vista principal3 'leermedida'
        


class MedidaDetalle (DetailView):
    model =Medida


class  MedidaActualizar(SuccessMessageMixin,UpdateView):
    model =  Medida
    form = Medida
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Medida' de nuestra Base de Datos 
    success_message = 'Medida Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal3:leermedida') # Redireccionamos a la vista principal3 'leermedida'
class MedidaEliminar(SuccessMessageMixin, DeleteView): 
    model = Medida
    form = Medida
    fields = "__all__"     
 
    # Redireccionamos a la página principal3 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Medida Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal3:leermedida') # Redireccionamos a la vista principal3 'leermedida'
    
#---------------------------Medida-----------------------------------#




#---------------------------Planificacion-----------------------------------#

class ListadoPlanificacion(CreateView,ListView,SuccessMessageMixin):
    model = Planificacion
    form = Planificacion
    fields = "__all__"
    success_message ='Planificacion creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal3:leerplanificacion') # Redireccionamos a la vista principal3 'leerplanificacion'
        


class PlanificacionDetalle (DetailView):
    model =Planificacion


class  PlanificacionActualizar(SuccessMessageMixin,UpdateView):
    model =  Planificacion
    form = Planificacion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Planificacion' de nuestra Base de Datos 
    success_message = 'Planificacion Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal3:leerplanificacion') # Redireccionamos a la vista principal3 'leerplanificacion'
class PlanificacionEliminar(SuccessMessageMixin, DeleteView): 
    model = Planificacion
    form = Planificacion
    fields = "__all__"     
 
    # Redireccionamos a la página principal3 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Planificacion Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal3:leerplanificacion') # Redireccionamos a la vista principal3 'leerplanificacion'
    
#---------------------------Planificacion-----------------------------------#



#---------------------------Receta-----------------------------------#

class ListadoReceta(CreateView,ListView,SuccessMessageMixin):
    model = Receta
    form = Receta
    fields = "__all__"
    success_message ='Receta creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal3:leerreceta') # Redireccionamos a la vista principal3 'leerreceta'
        


class RecetaDetalle (DetailView):
    model =Receta


class  RecetaActualizar(SuccessMessageMixin,UpdateView):
    model =  Receta
    form = Receta
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Receta' de nuestra Base de Datos 
    success_message = 'Receta Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal3:leerreceta') # Redireccionamos a la vista principal3 'leerreceta'
class RecetaEliminar(SuccessMessageMixin, DeleteView): 
    model = Receta
    form = Receta
    fields = "__all__"     
 
    # Redireccionamos a la página principal3 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Receta Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal3:leerreceta') # Redireccionamos a la vista principal3 'leerreceta'
    
#---------------------------Receta-----------------------------------#



#---------------------------Repeticion-----------------------------------#

class ListadoRepeticion(CreateView,ListView,SuccessMessageMixin):
    model = Repeticion
    form = Repeticion
    fields = "__all__"
    success_message ='Repeticion creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal3:leerrepeticion') # Redireccionamos a la vista principal3 'leerrepeticion'
        


class RepeticionDetalle (DetailView):
    model =Repeticion


class  RepeticionActualizar(SuccessMessageMixin,UpdateView):
    model =  Repeticion
    form = Repeticion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Repeticion' de nuestra Base de Datos 
    success_message = 'Repeticion Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal3:leerrepeticion') # Redireccionamos a la vista principal3 'leerrepeticion'
class RepeticionEliminar(SuccessMessageMixin, DeleteView): 
    model = Repeticion
    form = Repeticion
    fields = "__all__"     
 
    # Redireccionamos a la página principal3 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Repeticion Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal3:leerrepeticion') # Redireccionamos a la vista principal3 'leerrepeticion'
    
#---------------------------Repeticion-----------------------------------#



#---------------------------Rutina-----------------------------------#

class ListadoRutina(CreateView,ListView,SuccessMessageMixin):
    model = Rutina
    form = Rutina
    fields = "__all__"
    success_message ='Rutina creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal3:leerrutina') # Redireccionamos a la vista principal3 'leerrutina'
        


class RutinaDetalle (DetailView):
    model =Rutina


class  RutinaActualizar(SuccessMessageMixin,UpdateView):
    model =  Rutina
    form = Rutina
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Rutina' de nuestra Base de Datos 
    success_message = 'Rutina Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal3:leerrutina') # Redireccionamos a la vista principal3 'leerrutina'
class RutinaEliminar(SuccessMessageMixin, DeleteView): 
    model = Rutina
    form = Rutina
    fields = "__all__"     
 
    # Redireccionamos a la página principal3 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Rutina Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal3:leerrutina') # Redireccionamos a la vista principal3 'leerrutina'
    
#---------------------------Rutina-----------------------------------#



#---------------------------Serie-----------------------------------#

class ListadoSerie(CreateView,ListView,SuccessMessageMixin):
    model = Serie
    form = Serie
    fields = "__all__"
    success_message ='Serie creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal3:leerserie') # Redireccionamos a la vista principal3 'leerserie'
        


class SerieDetalle (DetailView):
    model =Serie


class  SerieActualizar(SuccessMessageMixin,UpdateView):
    model =  Serie
    form = Serie
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Serie' de nuestra Base de Datos 
    success_message = 'Serie Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal3:leerserie') # Redireccionamos a la vista principal3 'leerserie'
class SerieEliminar(SuccessMessageMixin, DeleteView): 
    model = Serie
    form = Serie
    fields = "__all__"     
 
    # Redireccionamos a la página principal3 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Serie Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal3:leerserie') # Redireccionamos a la vista principal3 'leerserie'
    
#---------------------------Serie-----------------------------------#



#---------------------------Tipoalimento-----------------------------------#

class ListadoTipoalimento(CreateView,ListView,SuccessMessageMixin):
    model = Tipoalimento
    form = Tipoalimento
    fields = "__all__"
    success_message ='Tipoalimento creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal3:leertipoalimento') # Redireccionamos a la vista principal3 'leertipoalimento'
        


class TipoalimentoDetalle (DetailView):
    model =Tipoalimento


class  TipoalimentoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipoalimento
    form = Tipoalimento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Tipoalimento' de nuestra Base de Datos 
    success_message = 'Tipoalimento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal3:leertipoalimento') # Redireccionamos a la vista principal3 'leertipoalimento'
class TipoalimentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipoalimento
    form = Tipoalimento
    fields = "__all__"     
 
    # Redireccionamos a la página principal3 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Tipoalimento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal3:leertipoalimento') # Redireccionamos a la vista principal3 'leertipoalimento'
    
#---------------------------Tipoalimento-----------------------------------#




#---------------------------Tipocomida-----------------------------------#

class ListadoTipocomida(CreateView,ListView,SuccessMessageMixin):
    model = Tipocomida
    form = Tipocomida
    fields = "__all__"
    success_message ='Tipocomida creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal3:leertipocomida') # Redireccionamos a la vista principal3 'leertipocomida'
        


class TipocomidaDetalle (DetailView):
    model =Tipocomida


class  TipocomidaActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipocomida
    form = Tipocomida
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Tipocomida' de nuestra Base de Datos 
    success_message = 'Tipocomida Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal3:leertipocomida') # Redireccionamos a la vista principal3 'leertipocomida'
class TipocomidaEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipocomida
    form = Tipocomida
    fields = "__all__"     
 
    # Redireccionamos a la página principal3 luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Tipocomida Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal3:leertipocomida') # Redireccionamos a la vista principal3 'leertipocomida'
    
#---------------------------Tipocomida-----------------------------------#







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
from django.contrib.auth import authenticate,get_user_model,authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from .forms import *

# Create your views here.

def Login(request):
    return render (request, "login.html")

def Home(request):
    
    return render (request, "index.html")


def Parametros (request):
   return render (request, "crud/index.html")  

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.views.generic import CreateView, TemplateView

from .models import *

from .forms import SignUpForm
from django.contrib.auth.views import LoginView


class SignUpView(CreateView):
    model = AuthUser
    form_class = SignUpForm
    template_name = 'register.html'

    def Register(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('index')
    



 #---------------------------Cargo-----------------------------------#
 

class ListadoCargo(CreateView,ListView,SuccessMessageMixin):
    
    model = Cargo
    form = Cargo
    fields = "__all__"
    success_message ='Cargo creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leercargo') # Redireccionamos a la vista principal 'leercargo'


class CargoDetalle (DetailView):
    model =Cargo


class  CargoActualizar(SuccessMessageMixin,UpdateView):
    model =  Cargo
    form = Cargo
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'cargo' de nuestra Base de Datos 
    success_message = 'Cargo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar 


    def get_success_url(self):               
        return reverse('principal:leercargo') # Redireccionamos a la vista principal 'leercargo'
class CargoEliminar(SuccessMessageMixin, DeleteView): 
    model = Cargo
    form = Cargo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro 
    
    def get_success_url(self): 
        success_message = 'Cargo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leercargo') # Redireccionamos a la vista principal 'leercargo'
    
#---------------------------Cargo-----------------------------------#



#---------------------------Cita-----------------------------------#

class ListadoCita(CreateView,ListView,SuccessMessageMixin):
    model = Cita
    form = Cita
    fields = "__all__"
    success_message ='Cita creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leercita') # Redireccionamos a la vista principal 'leercita'
        


class CitaDetalle (DetailView):
    model =Cita


class  CitaActualizar(SuccessMessageMixin,UpdateView):
    model =  Cita
    form = Cita
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'cita' de nuestra Base de Datos 
    success_message = 'Cita Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leercita') # Redireccionamos a la vista principal 'leercita'
class CitaEliminar(SuccessMessageMixin, DeleteView): 
    model = Cita
    form = Cita
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Cita Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leercita') # Redireccionamos a la vista principal 'leercita'
    
#---------------------------Cita-----------------------------------#



#---------------------------dia-----------------------------------#

class ListadoDia(CreateView,ListView,SuccessMessageMixin):
    model = Dia
    form = Dia
    fields = "__all__"
    success_message ='dia creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerdia') # Redireccionamos a la vista principal 'leerDia'
        


class DiaDetalle (DetailView):
    model =Dia


class  DiaActualizar(SuccessMessageMixin,UpdateView):
    model =  Dia
    form = Dia
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Dia' de nuestra Base de Datos 
    success_message = 'Dia Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerdia') # Redireccionamos a la vista principal 'leerDia'
class DiaEliminar(SuccessMessageMixin, DeleteView): 
    model = Dia
    form = Dia
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Dia Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerdia') # Redireccionamos a la vista principal 'leerDia'
    
#---------------------------dia-----------------------------------#



#---------------------------Dieta-----------------------------------#

class ListadoDieta(CreateView,ListView,SuccessMessageMixin):
    model = Dieta
    form = Dieta
    fields = "__all__"
    success_message ='Dieta creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerdieta') # Redireccionamos a la vista principal 'leerdieta'
        


class DietaDetalle (DetailView):
    model =Dieta


class  DietaActualizar(SuccessMessageMixin,UpdateView):
    model =  Dieta
    form = Dieta
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Dieta' de nuestra Base de Datos 
    success_message = 'Dieta Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerdieta') # Redireccionamos a la vista principal 'leerdieta'
class DietaEliminar(SuccessMessageMixin, DeleteView): 
    model = Dieta
    form = Dieta
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Dieta Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerdieta') # Redireccionamos a la vista principal 'leerdieta'
    
#---------------------------Dieta-----------------------------------#



#---------------------------Ejercicio-----------------------------------#

class ListadoEjercicio(CreateView,ListView,SuccessMessageMixin):
    model = Ejercicio
    form = Ejercicio
    fields = "__all__"
    success_message ='Ejercicio creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerejercicio') # Redireccionamos a la vista principal 'leerejercicio'
        


class EjercicioDetalle (DetailView):
    model =Ejercicio


class  EjercicioActualizar(SuccessMessageMixin,UpdateView):
    model =  Ejercicio
    form = Ejercicio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Ejercicio' de nuestra Base de Datos 
    success_message = 'Ejercicio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerejercicio') # Redireccionamos a la vista principal 'leerejercicio'
class EjercicioEliminar(SuccessMessageMixin, DeleteView): 
    model = Ejercicio
    form = Ejercicio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Ejercicio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerejercicio') # Redireccionamos a la vista principal 'leerejercicio'
    
#---------------------------Ejercicio-----------------------------------#



#---------------------------Enfoque-----------------------------------#

class ListadoEnfoque(CreateView,ListView,SuccessMessageMixin):
    model = Enfoque
    form = Enfoque
    fields = "__all__"
    success_message ='Enfoque creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerenfoque') # Redireccionamos a la vista principal 'leerenfoque'
        


class EnfoqueDetalle (DetailView):
    model =Enfoque


class  EnfoqueActualizar(SuccessMessageMixin,UpdateView):
    model =  Enfoque
    form = Enfoque
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Enfoque' de nuestra Base de Datos 
    success_message = 'Enfoque Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerenfoque') # Redireccionamos a la vista principal 'leerenfoque'
class EnfoqueEliminar(SuccessMessageMixin, DeleteView): 
    model = Enfoque
    form = Enfoque
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Enfoque Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerenfoque') # Redireccionamos a la vista principal 'leerenfoque'
    
#---------------------------Enfoque-----------------------------------#



#---------------------------Estado-----------------------------------#

class ListadoEstado(CreateView,ListView,SuccessMessageMixin):
    model = Estado
    form = Estado
    fields = "__all__"
    success_message ='Estado creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerestado') # Redireccionamos a la vista principal 'leerestado'
        


class EstadoDetalle (DetailView):
    model =Estado


class  EstadoActualizar(SuccessMessageMixin,UpdateView):
    model =  Estado
    form = Estado
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Estado' de nuestra Base de Datos 
    success_message = 'Estado Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerestado') # Redireccionamos a la vista principal 'leerestado'
class EstadoEliminar(SuccessMessageMixin, DeleteView): 
    model = Estado
    form = Estado
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Estado Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerestado') # Redireccionamos a la vista principal 'leerestado'
    
#---------------------------Estado-----------------------------------#



#---------------------------Evolucion-----------------------------------#

class ListadoEvolucion(CreateView,ListView,SuccessMessageMixin):
    model = Evolucion
    form = Evolucion
    fields = "__all__"
    success_message ='Evolucion creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerevolucion') # Redireccionamos a la vista principal 'leerevolucion'
        


class EvolucionDetalle (DetailView):
    model =Evolucion


class  EvolucionActualizar(SuccessMessageMixin,UpdateView):
    model =  Evolucion
    form = Evolucion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Evolucion' de nuestra Base de Datos 
    success_message = 'Evolucion Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerevolucion') # Redireccionamos a la vista principal 'leerevolucion'
class EvolucionEliminar(SuccessMessageMixin, DeleteView): 
    model = Evolucion
    form = Evolucion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Evolucion Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerevolucion') # Redireccionamos a la vista principal 'leerevolucion'
    
#---------------------------Evolucion-----------------------------------#



#---------------------------Genero-----------------------------------#

class ListadoGenero(CreateView,ListView,SuccessMessageMixin):
    model = Genero
    form = Genero
    fields = "__all__"
    success_message ='Genero creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leergenero') # Redireccionamos a la vista principal 'leergenero'
        


class GeneroDetalle (DetailView):
    model =Genero


class  GeneroActualizar(SuccessMessageMixin,UpdateView):
    model =  Genero
    form = Genero
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Genero' de nuestra Base de Datos 
    success_message = 'Genero Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leergenero') # Redireccionamos a la vista principal 'leergenero'
class GeneroEliminar(SuccessMessageMixin, DeleteView): 
    model = Genero
    form = Genero
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Genero Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leergenero') # Redireccionamos a la vista principal 'leergenero'
    
#---------------------------Genero-----------------------------------#



#---------------------------Historia-----------------------------------#

class ListadoHistoria(CreateView,ListView,SuccessMessageMixin):
    model = Historia
    form = Historia
    fields = "__all__"
    success_message ='Historia creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerhistoria') # Redireccionamos a la vista principal 'leerhistoria'
        


class HistoriaDetalle (DetailView):
    model =Historia


class  HistoriaActualizar(SuccessMessageMixin,UpdateView):
    model =  Historia
    form = Historia
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Historia' de nuestra Base de Datos 
    success_message = 'Historia Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerhistoria') # Redireccionamos a la vista principal 'leerhistoria'
class HistoriaEliminar(SuccessMessageMixin, DeleteView): 
    model = Historia
    form = Historia
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Historia Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerhistoria') # Redireccionamos a la vista principal 'leerhistoria'
    
#---------------------------Historia-----------------------------------#



#---------------------------Horario-----------------------------------#

class ListadoHorario(CreateView,ListView,SuccessMessageMixin):
    model = Horario
    form = Horario
    fields = "__all__"
    success_message ='Horario creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerhorario') # Redireccionamos a la vista principal 'leerhorario'
        


class HorarioDetalle (DetailView):
    model =Horario


class  HorarioActualizar(SuccessMessageMixin,UpdateView):
    model =  Horario
    form = Horario
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Horario' de nuestra Base de Datos 
    success_message = 'Horario Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerhorario') # Redireccionamos a la vista principal 'leerhorario'
class HorarioEliminar(SuccessMessageMixin, DeleteView): 
    model = Horario
    form = Horario
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Horario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerhorario') # Redireccionamos a la vista principal 'leerhorario'
    
#---------------------------Horario-----------------------------------#



#---------------------------Ingrediente-----------------------------------#

class ListadoIngrediente(CreateView,ListView,SuccessMessageMixin):
    model = Ingrediente
    form = Ingrediente
    fields = "__all__"
    success_message ='Ingrediente creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leeringrediente') # Redireccionamos a la vista principal 'leeringrediente'
        


class IngredienteDetalle (DetailView):
    model =Ingrediente


class  IngredienteActualizar(SuccessMessageMixin,UpdateView):
    model =  Ingrediente
    form = Ingrediente
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Ingrediente' de nuestra Base de Datos 
    success_message = 'Ingrediente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leeringrediente') # Redireccionamos a la vista principal 'leeringrediente'
class IngredienteEliminar(SuccessMessageMixin, DeleteView): 
    model = Ingrediente
    form = Ingrediente
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Ingrediente Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leeringrediente') # Redireccionamos a la vista principal 'leeringrediente'
    
#---------------------------Ingrediente-----------------------------------#



#---------------------------Medida-----------------------------------#

class ListadoMedida(CreateView,ListView,SuccessMessageMixin):
    model = Medida
    form = Medida
    fields = "__all__"
    success_message ='Medida creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leermedida') # Redireccionamos a la vista principal 'leermedida'
        


class MedidaDetalle (DetailView):
    model =Medida


class  MedidaActualizar(SuccessMessageMixin,UpdateView):
    model =  Medida
    form = Medida
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Medida' de nuestra Base de Datos 
    success_message = 'Medida Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leermedida') # Redireccionamos a la vista principal 'leermedida'
class MedidaEliminar(SuccessMessageMixin, DeleteView): 
    model = Medida
    form = Medida
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Medida Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leermedida') # Redireccionamos a la vista principal 'leermedida'
    
#---------------------------Medida-----------------------------------#



#---------------------------Ocupacion-----------------------------------#

class ListadoOcupacion(CreateView,ListView,SuccessMessageMixin):
    model = Ocupacion
    form = Ocupacion
    fields = "__all__"
    success_message ='Ocupacion creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerocupacion') # Redireccionamos a la vista principal 'leerocupacion'
        


class OcupacionDetalle (DetailView):
    model =Ocupacion


class  OcupacionActualizar(SuccessMessageMixin,UpdateView):
    model =  Ocupacion
    form = Ocupacion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Ocupacion' de nuestra Base de Datos 
    success_message = 'Ocupacion Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerocupacion') # Redireccionamos a la vista principal 'leerocupacion'
class OcupacionEliminar(SuccessMessageMixin, DeleteView): 
    model = Ocupacion
    form = Ocupacion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Ocupacion Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerocupacion') # Redireccionamos a la vista principal 'leerocupacion'
    
#---------------------------Ocupacion-----------------------------------#



#---------------------------Persona-----------------------------------#

class ListadoPersona(CreateView,ListView,SuccessMessageMixin):
    model = Persona
    form = Persona
    fields = "__all__"
    success_message ='Persona creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerpersona') # Redireccionamos a la vista principal 'leerpersona'
        


class PersonaDetalle (DetailView):
    model =Persona


class  PersonaActualizar(SuccessMessageMixin,UpdateView):
    model =  Persona
    form = Persona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Persona' de nuestra Base de Datos 
    success_message = 'Persona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerpersona') # Redireccionamos a la vista principal 'leerpersona'
class PersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Persona
    form = Persona
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Persona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerpersona') # Redireccionamos a la vista principal 'leerpersona'
    
#---------------------------Persona-----------------------------------#



#---------------------------Plan-----------------------------------#

class ListadoPlan(CreateView,ListView,SuccessMessageMixin):
    model = Plan
    form = Plan
    fields = "__all__"
    success_message ='Plan creado correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerplan') # Redireccionamos a la vista principal 'leerplan'
        


class PlanDetalle (DetailView):
    model =Plan


class  PlanActualizar(SuccessMessageMixin,UpdateView):
    model =  Plan
    form = Plan
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Plan' de nuestra Base de Datos 
    success_message = 'Plan Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerplan') # Redireccionamos a la vista principal 'leerplan'
class PlanEliminar(SuccessMessageMixin, DeleteView): 
    model = Plan
    form = Plan
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Plan Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerplan') # Redireccionamos a la vista principal 'leerplan'
    
#---------------------------Plan-----------------------------------#



#---------------------------Planificacion-----------------------------------#

class ListadoPlanificacion(CreateView,ListView,SuccessMessageMixin):
    model = Planificacion
    form = Planificacion
    fields = "__all__"
    success_message ='Planificacion creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerplanificacion') # Redireccionamos a la vista principal 'leerplanificacion'
        


class PlanificacionDetalle (DetailView):
    model =Planificacion


class  PlanificacionActualizar(SuccessMessageMixin,UpdateView):
    model =  Planificacion
    form = Planificacion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Planificacion' de nuestra Base de Datos 
    success_message = 'Planificacion Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerplanificacion') # Redireccionamos a la vista principal 'leerplanificacion'
class PlanificacionEliminar(SuccessMessageMixin, DeleteView): 
    model = Planificacion
    form = Planificacion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Planificacion Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerplanificacion') # Redireccionamos a la vista principal 'leerplanificacion'
    
#---------------------------Planificacion-----------------------------------#



#---------------------------Receta-----------------------------------#

class ListadoReceta(CreateView,ListView,SuccessMessageMixin):
    model = Receta
    form = Receta
    fields = "__all__"
    success_message ='Receta creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerreceta') # Redireccionamos a la vista principal 'leerreceta'
        


class RecetaDetalle (DetailView):
    model =Receta


class  RecetaActualizar(SuccessMessageMixin,UpdateView):
    model =  Receta
    form = Receta
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Receta' de nuestra Base de Datos 
    success_message = 'Receta Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerreceta') # Redireccionamos a la vista principal 'leerreceta'
class RecetaEliminar(SuccessMessageMixin, DeleteView): 
    model = Receta
    form = Receta
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Receta Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerreceta') # Redireccionamos a la vista principal 'leerreceta'
    
#---------------------------Receta-----------------------------------#



#---------------------------Repeticion-----------------------------------#

class ListadoRepeticion(CreateView,ListView,SuccessMessageMixin):
    model = Repeticion
    form = Repeticion
    fields = "__all__"
    success_message ='Repeticion creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerrepeticion') # Redireccionamos a la vista principal 'leerrepeticion'
        


class RepeticionDetalle (DetailView):
    model =Repeticion


class  RepeticionActualizar(SuccessMessageMixin,UpdateView):
    model =  Repeticion
    form = Repeticion
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Repeticion' de nuestra Base de Datos 
    success_message = 'Repeticion Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerrepeticion') # Redireccionamos a la vista principal 'leerrepeticion'
class RepeticionEliminar(SuccessMessageMixin, DeleteView): 
    model = Repeticion
    form = Repeticion
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Repeticion Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerrepeticion') # Redireccionamos a la vista principal 'leerrepeticion'
    
#---------------------------Repeticion-----------------------------------#



#---------------------------Rutina-----------------------------------#

class ListadoRutina(CreateView,ListView,SuccessMessageMixin):
    model = Rutina
    form = Rutina
    fields = "__all__"
    success_message ='Rutina creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerrutina') # Redireccionamos a la vista principal 'leerrutina'
        


class RutinaDetalle (DetailView):
    model =Rutina


class  RutinaActualizar(SuccessMessageMixin,UpdateView):
    model =  Rutina
    form = Rutina
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Rutina' de nuestra Base de Datos 
    success_message = 'Rutina Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerrutina') # Redireccionamos a la vista principal 'leerrutina'
class RutinaEliminar(SuccessMessageMixin, DeleteView): 
    model = Rutina
    form = Rutina
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Rutina Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerrutina') # Redireccionamos a la vista principal 'leerrutina'
    
#---------------------------Rutina-----------------------------------#



#---------------------------Serie-----------------------------------#

class ListadoSerie(CreateView,ListView,SuccessMessageMixin):
    model = Serie
    form = Serie
    fields = "__all__"
    success_message ='Serie creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerserie') # Redireccionamos a la vista principal 'leerserie'
        


class SerieDetalle (DetailView):
    model =Serie


class  SerieActualizar(SuccessMessageMixin,UpdateView):
    model =  Serie
    form = Serie
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Serie' de nuestra Base de Datos 
    success_message = 'Serie Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerserie') # Redireccionamos a la vista principal 'leerserie'
class SerieEliminar(SuccessMessageMixin, DeleteView): 
    model = Serie
    form = Serie
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Serie Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerserie') # Redireccionamos a la vista principal 'leerserie'
    
#---------------------------Serie-----------------------------------#



#---------------------------Tipocomida-----------------------------------#

class ListadoTipocomida(CreateView,ListView,SuccessMessageMixin):
    model = Tipocomida
    form = Tipocomida
    fields = "__all__"
    success_message ='Tipocomida creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leertipocomida') # Redireccionamos a la vista principal 'leertipocomida'
        


class TipocomidaDetalle (DetailView):
    model =Tipocomida


class  TipocomidaActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipocomida
    form = Tipocomida
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Tipocomida' de nuestra Base de Datos 
    success_message = 'Tipocomida Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leertipocomida') # Redireccionamos a la vista principal 'leertipocomida'
class TipocomidaEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipocomida
    form = Tipocomida
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Tipocomida Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leertipocomida') # Redireccionamos a la vista principal 'leertipocomida'
    
#---------------------------Tipocomida-----------------------------------#



#---------------------------Tipodocumento-----------------------------------#

class ListadoTipodocumento(CreateView,ListView,SuccessMessageMixin):
    model = Tipodocumento
    form = Tipodocumento
    fields = "__all__"
    success_message ='Tipodocumento creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leertipodocumento') # Redireccionamos a la vista principal 'leertipodocumento'
        


class TipodocumentoDetalle (DetailView):
    model =Tipodocumento


class  TipodocumentoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipodocumento
    form = Tipodocumento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Tipodocumento' de nuestra Base de Datos 
    success_message = 'Tipodocumento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leertipodocumento') # Redireccionamos a la vista principal 'leertipodocumento'
class TipodocumentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipodocumento
    form = Tipodocumento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Tipodocumento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leertipodocumento') # Redireccionamos a la vista principal 'leertipodocumento'
    
#---------------------------Tipodocumento-----------------------------------#



#---------------------------Tipopersona-----------------------------------#

class ListadoTipopersona(CreateView,ListView,SuccessMessageMixin):
    model = Tipopersona
    form = Tipopersona
    fields = "__all__"
    success_message ='Tipopersona creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leertipersona') # Redireccionamos a la vista principal 'leertipersona'
        


class TipopersonaDetalle (DetailView):
    model =Tipopersona


class  TipopersonaActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipopersona
    form = Tipopersona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Tipopersona' de nuestra Base de Datos 
    success_message = 'Tipopersona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leertipersona') # Redireccionamos a la vista principal 'leertipersona'
class TipopersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipopersona
    form = Tipopersona
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Tipopersona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leertipersona') # Redireccionamos a la vista principal 'leertipersona'
    
#---------------------------Tipopersona-----------------------------------#



#---------------------------Tipoplan-----------------------------------#

class ListadoTipoplan(CreateView,ListView,SuccessMessageMixin):
    model = Tipoplan
    form = Tipoplan
    fields = "__all__"
    success_message ='Tipoplan creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leertipoplan') # Redireccionamos a la vista principal 'leertipoplan'
        


class TipoplanDetalle (DetailView):
    model =Tipoplan


class  TipoplanActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipoplan
    form = Tipoplan
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Tipoplan' de nuestra Base de Datos 
    success_message = 'Tipoplan Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leertipoplan') # Redireccionamos a la vista principal 'leertipoplan'
class TipoplanEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipoplan
    form = Tipoplan
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Tipoplan Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leertipoplan') # Redireccionamos a la vista principal 'leertipoplan'
    
#---------------------------Tipoplan-----------------------------------#



#---------------------------Tipoalimento-----------------------------------#

class ListadoTipoalimento(CreateView,ListView,SuccessMessageMixin):
    model = Tipoalimento
    form = Tipoalimento
    fields = "__all__"
    success_message ='Tipoalimento creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leertipoalimento') # Redireccionamos a la vista principal 'leertipoalimento'
        


class TipoalimentoDetalle (DetailView):
    model =Tipoalimento


class  TipoalimentoActualizar(SuccessMessageMixin,UpdateView):
    model =  Tipoalimento
    form = Tipoalimento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Tipoalimento' de nuestra Base de Datos 
    success_message = 'Tipoalimento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leertipoalimento') # Redireccionamos a la vista principal 'leertipoalimento'
class TipoalimentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Tipoalimento
    form = Tipoalimento
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Tipoalimento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leertipoalimento') # Redireccionamos a la vista principal 'leertipoalimento'
    
#---------------------------Tipoalimento-----------------------------------#



#---------------------------Usuario-----------------------------------#

class ListadoUsuario(CreateView,ListView,SuccessMessageMixin):
    model = Usuario
    form = Usuario
    fields = "__all__"
    success_message ='Usuario creada correctamente'
     
    def get_success_url(self):        
        return reverse('principal:leerusuario') # Redireccionamos a la vista principal 'leerusuario'
        


class UsuarioDetalle (DetailView):
    model =Usuario


class  UsuarioActualizar(SuccessMessageMixin,UpdateView):
    model =  Usuario
    form = Usuario
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Usuario' de nuestra Base de Datos 
    success_message = 'Usuario Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un "dato" 


    def get_success_url(self):               
        return reverse('principal:leerusuario') # Redireccionamos a la vista principal 'leerusuario'
class UsuarioEliminar(SuccessMessageMixin, DeleteView): 
    model = Usuario
    form = Usuario
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o "dato"
    
    def get_success_url(self): 
        success_message = 'Usuario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un dato 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerusuario') # Redireccionamos a la vista principal 'leerusuario'
    
#---------------------------Usuario-----------------------------------#





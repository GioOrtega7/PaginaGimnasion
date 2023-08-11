from django.contrib import admin
from django.urls import path
from principal.views import *

urlpatterns = [ 
    
                                                          ## Inicio De Tienda ##




##-----------------------------------------------------------ZZZZZ---------------------------------------------------------------##

   #path('zzz/', ListadoZZZZZ.as_view(template_name = "crud/zzz/tables.html"), name='leerzzz'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   #path ('zzz/detalle/<int:pk>', ZZZZZDetalle.as_view(template_name = "crud/zzz/detalle.html"), name='detallezzz'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   #path('zzz/editar/<int:pk>', ZZZZZActualizar.as_view(template_name = "crud/zzz/actualizar.html"), name='actualizarzzz'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   #path('zzz/eliminar/<int:pk>', ZZZZZEliminar.as_view(template_name ='crud/zzz/eliminar.html')), 

##---------------------------------------------------------ZZZZZ------------------------------------------------------------##



                                                         ## Fin De Crud ##



 

]
from django.contrib import admin
from django.urls import path
from principal.views1 import *

urlpatterns = [ 
    
                                                          ## Inicio De GENERAL ##

##----------------------------------------------------------Cargo---------------------------------------------------------------##

   path('cargo/', ListadoCargo.as_view(template_name = "GENERAL/cargo/tables.html"), name='leercargo'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cargo registro 
   path('cargo/detalle/<int:pk>', CargoDetalle.as_view(template_name = "GENERAL/cargo/detalle.html"), name='detallecargo'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cargo o registro  
   #path('cargo/crear', CargoCrear.as_view(template_name = "GENERAL/cargo/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cargo registro de la Base de Datos 
   path('cargo/editar/<int:pk>', CargoActualizar.as_view(template_name = "GENERAL/cargo/actualizar.html"), name='actualizarcargo'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cargo o registro de la Base de Datos 
   path('cargo/eliminar/<int:pk>', CargoEliminar.as_view(template_name ='GENERAL/cargo/eliminar.html')), 

##----------------------------------------------------------Cargo---------------------------------------------------------------##


   

##-----------------------------------------------------------Estado---------------------------------------------------------------##

   path('estado/', ListadoEstado.as_view(template_name = "GENERAL/estado/tables.html"), name='leerestado'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('estado/detalle/<int:pk>', EstadoDetalle.as_view(template_name = "GENERAL/estado/detalle.html"), name='detalleestado'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "GENERAL/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('estado/editar/<int:pk>', EstadoActualizar.as_view(template_name = "GENERAL/estado/actualizar.html"), name='actualizarestado'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('estado/eliminar/<int:pk>', EstadoEliminar.as_view(template_name ='GENERAL/estado/eliminar.html')), 

##---------------------------------------------------------Estado---------------------------------------------------------------##







##-----------------------------------------------------------Genero---------------------------------------------------------------##

   path('genero/', ListadoGenero.as_view(template_name = "GENERAL/genero/tables.html"), name='leergenero'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('genero/detalle/<int:pk>', GeneroDetalle.as_view(template_name = "GENERAL/genero/detalle.html"), name='detallegenero'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "GENERAL/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('genero/editar/<int:pk>', GeneroActualizar.as_view(template_name = "GENERAL/genero/actualizar.html"), name='actualizargenero'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('genero/eliminar/<int:pk>', GeneroEliminar.as_view(template_name ='GENERAL/genero/eliminar.html')), 

##---------------------------------------------------------Genero---------------------------------------------------------------##






##-----------------------------------------------------------Ocupacion---------------------------------------------------------------##

   path('ocupacion/', ListadoOcupacion.as_view(template_name = "GENERAL/ocupacion/tables.html"), name='leerocupacion'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('ocupacion/detalle/<int:pk>', OcupacionDetalle.as_view(template_name = "GENERAL/ocupacion/detalle.html"), name='detalleocupacion'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "GENERAL/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('ocupacion/editar/<int:pk>', OcupacionActualizar.as_view(template_name = "GENERAL/ocupacion/actualizar.html"), name='actualizarocupacion'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('ocupacion/eliminar/<int:pk>', OcupacionEliminar.as_view(template_name ='GENERAL/ocupacion/eliminar.html')), 

##---------------------------------------------------------Ocupacion---------------------------------------------------------------##



##-----------------------------------------------------------Persona---------------------------------------------------------------##

   path('persona/', ListadoPersona.as_view(template_name = "GENERAL/persona/tables.html"), name='leerpersona'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('persona/detalle/<int:pk>', PersonaDetalle.as_view(template_name = "GENERAL/persona/detalle.html"), name='detallepersona'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "GENERAL/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "GENERAL/persona/actualizar.html"), name='actualizarpersona'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('persona/eliminar/<int:pk>', PersonaEliminar.as_view(template_name ='GENERAL/persona/eliminar.html')), 

##---------------------------------------------------------Persona---------------------------------------------------------------##






##-----------------------------------------------------------Tipodocumento---------------------------------------------------------------##

   path('tipodocumento/', ListadoTipodocumento.as_view(template_name = "GENERAL/tipodocumento/tables.html"), name='leertipodocumento'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('tipodocumento/detalle/<int:pk>', TipodocumentoDetalle.as_view(template_name = "GENERAL/tipodocumento/detalle.html"), name='detalletipodocumento'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "GENERAL/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('tipodocumento/editar/<int:pk>', TipodocumentoActualizar.as_view(template_name = "GENERAL/tipodocumento/actualizar.html"), name='actualizartipodocumento'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('tipodocumento/eliminar/<int:pk>', TipodocumentoEliminar.as_view(template_name ='GENERAL/tipodocumento/eliminar.html')), 

##---------------------------------------------------------Tipodocumento------------------------------------------------------------##



##-----------------------------------------------------------Tipopersona---------------------------------------------------------------##

   path('tipopersona/', ListadoTipopersona.as_view(template_name = "GENERAL/tipopersona/tables.html"), name='leertipopersona'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('tipopersona/detalle/<int:pk>', TipopersonaDetalle.as_view(template_name = "GENERAL/tipopersona/detalle.html"), name='detalletipopersona'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "GENERAL/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('tipopersona/editar/<int:pk>', TipopersonaActualizar.as_view(template_name = "GENERAL/tipopersona/actualizar.html"), name='actualizartipopersona'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('tipopersona/eliminar/<int:pk>', TipopersonaEliminar.as_view(template_name ='GENERAL/tipopersona/eliminar.html')), 

##---------------------------------------------------------Tipopersona------------------------------------------------------------##





##-----------------------------------------------------------Usuario---------------------------------------------------------------##

   path('usuario/', ListadoUsuario.as_view(template_name = "GENERAL/usuario/tables.html"), name='leerusuario'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('usuario/detalle/<int:pk>', UsuarioDetalle.as_view(template_name = "GENERAL/usuario/detalle.html"), name='detalleusuario'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "GENERAL/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('usuario/editar/<int:pk>', UsuarioActualizar.as_view(template_name = "GENERAL/usuario/actualizar.html"), name='actualizarusuario'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('usuario/eliminar/<int:pk>', UsuarioEliminar.as_view(template_name ='GENERAL/usuario/eliminar.html')), 

##---------------------------------------------------------Usuario------------------------------------------------------------##

##-----------------------------------------------------------ZZZZZ---------------------------------------------------------------##

   #path('zzz/', ListadoZZZZZ.as_view(template_name = "GENERAL/zzz/tables.html"), name='leerzzz'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   #path ('zzz/detalle/<int:pk>', ZZZZZDetalle.as_view(template_name = "GENERAL/zzz/detalle.html"), name='detallezzz'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "GENERAL/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   #path('zzz/editar/<int:pk>', ZZZZZActualizar.as_view(template_name = "GENERAL/zzz/actualizar.html"), name='actualizarzzz'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   #path('zzz/eliminar/<int:pk>', ZZZZZEliminar.as_view(template_name ='GENERAL/zzz/eliminar.html')), 

##---------------------------------------------------------ZZZZZ------------------------------------------------------------##



                                                         ## Fin De GENERAL ##




]
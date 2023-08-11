from django.contrib import admin
from django.urls import path
from principal.views3 import *

urlpatterns = [ 
    
                                                          ## Inicio De PROGRAMA ##





##-----------------------------------------------------------Dieta---------------------------------------------------------------##

   path('dieta/',ListadoDieta.as_view(template_name = "PROGRAMA/dieta/tables.html"), name='leerdieta'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('dieta/detalle/<int:pk>', DietaDetalle.as_view(template_name = "PROGRAMA/dieta/detalle.html"), name='detalledieta'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "PROGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('dieta/editar/<int:pk>', DietaActualizar.as_view(template_name = "PROGRAMA/dieta/actualizar.html"), name='actualizardia'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('dieta/eliminar/<int:pk>', DietaEliminar.as_view(template_name ='PROGRAMA/dieta/eliminar.html')), 

##----------------------------------------------------------Dieta---------------------------------------------------------------##



##-----------------------------------------------------------Ejercicio---------------------------------------------------------------##

   path('ejercicio/', ListadoEjercicio.as_view(template_name = "PROGRAMA/ejercicio/tables.html"), name='leerejercicio'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path('ejercicio/detalle/<int:pk>', EjercicioDetalle.as_view(template_name = "PROGRAMA/ejercicio/detalle.html"), name='detalleejercicio'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "PROGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('ejercicio/editar/<int:pk>',EjercicioActualizar.as_view(template_name = "PROGRAMA/ejercicio/actualizar.html"), name='actualizarejercicio'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('ejercicio/eliminar/<int:pk>',EjercicioEliminar.as_view(template_name ='PROGRAMA/ejercicio/eliminar.html')), 

##----------------------------------------------------------Ejercicio---------------------------------------------------------------##





##-----------------------------------------------------------Ingrediente---------------------------------------------------------------##

   path('ingrediente/', ListadoIngrediente.as_view(template_name = "PROGRAMA/ingrediente/tables.html"), name='leeringrediente'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('ingrediente/detalle/<int:pk>', IngredienteDetalle.as_view(template_name = "PROGRAMA/ingrediente/detalle.html"), name='detalleingrediente'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "PROGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('ingrediente/editar/<int:pk>', IngredienteActualizar.as_view(template_name = "PROGRAMA/ingrediente/actualizar.html"), name='actualizaringrediente'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('ingrediente/eliminar/<int:pk>', IngredienteEliminar.as_view(template_name ='PROGRAMA/ingrediente/eliminar.html')), 

##---------------------------------------------------------Ingrediente---------------------------------------------------------------##



##-----------------------------------------------------------Medida---------------------------------------------------------------##

   path('medida/', ListadoMedida.as_view(template_name = "PROGRAMA/medida/tables.html"), name='leermedida'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('medida/detalle/<int:pk>', MedidaDetalle.as_view(template_name = "PROGRAMA/medida/detalle.html"), name='detallemedida'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "PROGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('medida/editar/<int:pk>', MedidaActualizar.as_view(template_name = "PROGRAMA/medida/actualizar.html"), name='actualizarmedida'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('medida/eliminar/<int:pk>', MedidaEliminar.as_view(template_name ='PROGRAMA/medida/eliminar.html')), 

##---------------------------------------------------------Medida------------------------------------------------------Medida








##-----------------------------------------------------------Planificacion---------------------------------------------------------------##

   path('planificacion/', ListadoPlanificacion.as_view(template_name = "PROGRAMA/planificacion/tables.html"), name='leerplanificacion'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('planificacion/detalle/<int:pk>', PlanificacionDetalle.as_view(template_name = "PROGRAMA/planificacion/detalle.html"), name='detalleplanificacion'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "PROGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('planificacion/editar/<int:pk>', PlanificacionActualizar.as_view(template_name = "PROGRAMA/planificacion/actualizar.html"), name='actualizarplanificacion'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('planificacion/eliminar/<int:pk>', PlanificacionEliminar.as_view(template_name ='PROGRAMA/planificacion/eliminar.html')), 

##---------------------------------------------------------Planificacion---------------------------------------------------------------##



##-----------------------------------------------------------Receta---------------------------------------------------------------##

   path('receta/', ListadoReceta.as_view(template_name = "PROGRAMA/receta/tables.html"), name='leerreceta'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('receta/detalle/<int:pk>', RecetaDetalle.as_view(template_name = "PROGRAMA/receta/detalle.html"), name='detallereceta'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "PROGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('receta/editar/<int:pk>', RecetaActualizar.as_view(template_name = "PROGRAMA/receta/actualizar.html"), name='actualizarreceta'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('receta/eliminar/<int:pk>', RecetaEliminar.as_view(template_name ='PROGRAMA/receta/eliminar.html')), 

##---------------------------------------------------------Receta---------------------------------------------------------------##



##-----------------------------------------------------------Repeticion---------------------------------------------------------------##

   path('repeticion/', ListadoRepeticion.as_view(template_name = "PROGRAMA/repeticion/tables.html"), name='leerrepeticion'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('repeticion/detalle/<int:pk>', RepeticionDetalle.as_view(template_name = "PROGRAMA/repeticion/detalle.html"), name='detallerepeticion'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "PROGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('repeticion/editar/<int:pk>', RepeticionActualizar.as_view(template_name = "PROGRAMA/repeticion/actualizar.html"), name='actualizarrepeticion'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('repeticion/eliminar/<int:pk>', RepeticionEliminar.as_view(template_name ='PROGRAMA/repeticion/eliminar.html')), 

##---------------------------------------------------------Repeticion---------------------------------------------------------------##



##-----------------------------------------------------------Rutina---------------------------------------------------------------##

   path('rutina/', ListadoRutina.as_view(template_name = "PROGRAMA/rutina/tables.html"), name='leerrutina'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('rutina/detalle/<int:pk>', RutinaDetalle.as_view(template_name = "PROGRAMA/rutina/detalle.html"), name='detallerutina'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "PROGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('rutina/editar/<int:pk>', RutinaActualizar.as_view(template_name = "PROGRAMA/rutina/actualizar.html"), name='actualizarrutina'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('rutina/eliminar/<int:pk>', RutinaEliminar.as_view(template_name ='PROGRAMA/rutina/eliminar.html')), 

##---------------------------------------------------------Rutina------------------------------------------------------------##



##-----------------------------------------------------------Serie---------------------------------------------------------------##

   path('serie/', ListadoSerie.as_view(template_name = "PROGRAMA/serie/tables.html"), name='leerserie'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('serie/detalle/<int:pk>', SerieDetalle.as_view(template_name = "PROGRAMA/serie/detalle.html"), name='detalleserie'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "PROGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('serie/editar/<int:pk>', SerieActualizar.as_view(template_name = "PROGRAMA/serie/actualizar.html"), name='actualizarserie'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('serie/eliminar/<int:pk>', SerieEliminar.as_view(template_name ='PROGRAMA/serie/eliminar.html')), 

##---------------------------------------------------------Serie------------------------------------------------------------##





##-----------------------------------------------------------Tipoalimento---------------------------------------------------------------##

   path('tipoalimento/', ListadoTipoalimento.as_view(template_name = "PROGRAMA/tipoalimento/tables.html"), name='leertipoalimento'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('tipoalimento/detalle/<int:pk>', TipoalimentoDetalle.as_view(template_name = "PROGRAMA/tipoalimento/detalle.html"), name='detalletipoalimento'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "PROGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('tipoalimento/editar/<int:pk>', TipoalimentoActualizar.as_view(template_name = "PROGRAMA/tipoalimento/actualizar.html"), name='actualizartipoalimento'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('tipoalimento/eliminar/<int:pk>', TipoalimentoEliminar.as_view(template_name ='PROGRAMA/tipoalimento/eliminar.html')), 

##---------------------------------------------------------Tipoalimento------------------------------------------------------------##



##-----------------------------------------------------------Tipocomida---------------------------------------------------------------##

   path('tipocomida/', ListadoTipocomida.as_view(template_name = "PROGRAMA/tipocomida/tables.html"), name='leertipocomida'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('tipocomida/detalle/<int:pk>', TipocomidaDetalle.as_view(template_name = "PROGRAMA/tipocomida/detalle.html"), name='detalletipocomida'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "PROGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('tipocomida/editar/<int:pk>', TipocomidaActualizar.as_view(template_name = "PROGRAMA/tipocomida/actualizar.html"), name='actualizartipocomida'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('tipocomida/eliminar/<int:pk>', TipocomidaEliminar.as_view(template_name ='PROGRAMA/tipocomida/eliminar.html')), 

##---------------------------------------------------------Tipocomida------------------------------------------------------------##



##-----------------------------------------------------------ZZZZZ---------------------------------------------------------------##

   #path('zzz/', ListadoZZZZZ.as_view(template_name = "PROGRAMA/zzz/tables.html"), name='leerzzz'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   #path ('zzz/detalle/<int:pk>', ZZZZZDetalle.as_view(template_name = "PROGRAMA/zzz/detalle.html"), name='detallezzz'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "PROGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   #path('zzz/editar/<int:pk>', ZZZZZActualizar.as_view(template_name = "PROGRAMA/zzz/actualizar.html"), name='actualizarzzz'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   #path('zzz/eliminar/<int:pk>', ZZZZZEliminar.as_view(template_name ='PROGRAMA/zzz/eliminar.html')), 

##---------------------------------------------------------ZZZZZ------------------------------------------------------------##



                                                         ## Fin De PROGRAMA ##





]
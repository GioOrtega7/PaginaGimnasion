from django.contrib import admin
from django.urls import path
from principal.views2 import *

urlpatterns = [ 
    
                                                          ## Inicio De CRONOGRAMA ##




   
##-----------------------------------------------------------Cita---------------------------------------------------------------##

   path('cita/', ListadoCita.as_view(template_name = "CRONOGRAMA/cita/tables.html"), name='leercita'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path('cita/detalle/<int:pk>', CitaDetalle.as_view(template_name = "CRONOGRAMA/cita/detalle.html"), name='detallecita'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "CRONOGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('cita/editar/<int:pk>', CitaActualizar.as_view(template_name = "CRONOGRAMA/cita/actualizar.html"), name='actualizarcita'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('cita/eliminar/<int:pk>', CitaEliminar.as_view(template_name ='CRONOGRAMA/cita/eliminar.html')), 

##----------------------------------------------------------cargo---------------------------------------------------------------##



##-----------------------------------------------------------Dia---------------------------------------------------------------##

   path('dia/', ListadoDia.as_view(template_name = "CRONOGRAMA/dia/tables.html"), name='leerdia'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path('dia/detalle/<int:pk>', DiaDetalle.as_view(template_name = "CRONOGRAMA/dia/detalle.html"), name='detalledia'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "CRONOGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('dia/editar/<int:pk>', DiaActualizar.as_view(template_name = "CRONOGRAMA/dia/actualizar.html"), name='actualizardia'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('dia/eliminar/<int:pk>', DiaEliminar.as_view(template_name ='CRONOGRAMA/dia/eliminar.html')), 

##----------------------------------------------------------Dia---------------------------------------------------------------##



##-----------------------------------------------------------Enfoque---------------------------------------------------------------##

   path('enfoque/', ListadoEnfoque.as_view(template_name = "CRONOGRAMA/enfoque/tables.html"), name='leerenfoque'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('enfoque/detalle/<int:pk>', EnfoqueDetalle.as_view(template_name = "CRONOGRAMA/enfoque/detalle.html"), name='detalleenfoque'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "CRONOGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('enfoque/editar/<int:pk>', EnfoqueActualizar.as_view(template_name = "CRONOGRAMA/enfoque/actualizar.html"), name='actualizarenfoque'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('enfoque/eliminar/<int:pk>', EnfoqueEliminar.as_view(template_name ='CRONOGRAMA/enfoque/eliminar.html')), 

##----------------------------------------------------------Enfoque---------------------------------------------------------------##




##-----------------------------------------------------------Evolucion---------------------------------------------------------------##

   path('evolucion/', ListadoEvolucion.as_view(template_name = "CRONOGRAMA/evolucion/tables.html"), name='leerevolucion'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('evolucion/detalle/<int:pk>', EvolucionDetalle.as_view(template_name = "CRONOGRAMA/evolucion/detalle.html"), name='detalleevolucion'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "CRONOGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('evolucion/editar/<int:pk>', EvolucionActualizar.as_view(template_name = "CRONOGRAMA/evolucion/actualizar.html"), name='actualizarevolucion'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('evolucion/eliminar/<int:pk>', EvolucionEliminar.as_view(template_name ='CRONOGRAMA/evolucion/eliminar.html')), 

##---------------------------------------------------------Evolucion---------------------------------------------------------------##





##-----------------------------------------------------------Historia---------------------------------------------------------------##

   path('historia/', ListadoHistoria.as_view(template_name = "CRONOGRAMA/historia/tables.html"), name='leerhistoria'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('historia/detalle/<int:pk>', HistoriaDetalle.as_view(template_name = "CRONOGRAMA/historia/detalle.html"), name='detallehistoria'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "CRONOGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('historia/editar/<int:pk>', HistoriaActualizar.as_view(template_name = "CRONOGRAMA/historia/actualizar.html"), name='actualizarhistoria'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('historia/eliminar/<int:pk>', HistoriaEliminar.as_view(template_name ='CRONOGRAMA/historia/eliminar.html')), 

##---------------------------------------------------------Historia---------------------------------------------------------------##



##-----------------------------------------------------------Horario---------------------------------------------------------------##

   path('horario/', ListadoHorario.as_view(template_name = "CRONOGRAMA/horario/tables.html"), name='leerhorario'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('horario/detalle/<int:pk>', HorarioDetalle.as_view(template_name = "CRONOGRAMA/horario/detalle.html"), name='detallehorario'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "CRONOGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('horario/editar/<int:pk>', HorarioActualizar.as_view(template_name = "CRONOGRAMA/horario/actualizar.html"), name='actualizarhorario'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('horario/eliminar/<int:pk>', HorarioEliminar.as_view(template_name ='CRONOGRAMA/horario/eliminar.html')), 

##---------------------------------------------------------Horario---------------------------------------------------------------##





##-----------------------------------------------------------Plan---------------------------------------------------------------##

   path('plan/', ListadoPlan.as_view(template_name = "CRONOGRAMA/plan/tables.html"), name='leerplan'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('plan/detalle/<int:pk>', PlanDetalle.as_view(template_name = "CRONOGRAMA/plan/detalle.html"), name='detalleplan'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "CRONOGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('plan/editar/<int:pk>', PlanActualizar.as_view(template_name = "CRONOGRAMA/plan/actualizar.html"), name='actualizarplan'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('plan/eliminar/<int:pk>', PlanEliminar.as_view(template_name ='CRONOGRAMA/plan/eliminar.html')), 

##---------------------------------------------------------Plan---------------------------------------------------------------##








##-----------------------------------------------------------Tipoplan---------------------------------------------------------------##

   path('tipoplan/', ListadoTipoplan.as_view(template_name = "CRONOGRAMA/tipoplan/tables.html"), name='leertipoplan'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('tipoplan/detalle/<int:pk>', TipoplanDetalle.as_view(template_name = "CRONOGRAMA/tipoplan/detalle.html"), name='detalletipoplan'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "CRONOGRAMA/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('tipoplan/editar/<int:pk>', TipoplanActualizar.as_view(template_name = "CRONOGRAMA/tipoplan/actualizar.html"), name='actualizartipoplan'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('tipoplan/eliminar/<int:pk>', TipoplanEliminar.as_view(template_name ='CRONOGRAMA/tipoplan/eliminar.html')), 

##---------------------------------------------------------Tipoplan------------------------------------------------------------##

##-----------------------------------------------------------Catalogo------------------------------------------------------------##

   path('catalogo/', ListadoTipoplan.as_view(template_name = 'CATALOGO/catalogo.html'), name='leercatalogo'),
   path('catalogo/', ListadoTipoplan.as_view(template_name = 'CATALOGO/tables.html'), name='creartipoplan'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Plan registro 
   path('catalogo/detalle/<int:pk>', TipoplanDetalle.as_view(template_name = 'CATALOGO/detalle.html'), name='detalletipoplan'),

 ##-----------------------------------------------------------Catalogo------------------------------------------------------------##

]
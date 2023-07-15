from django.contrib import admin
from django.urls import path
from principal.views import *

urlpatterns = [ 
    
                                                          ## Inicio De Crud ##

##----------------------------------------------------------Cargo---------------------------------------------------------------##

   path('cargo/', ListadoCargo.as_view(template_name = "crud/cargo/tables.html"), name='leercargo'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cargo registro 
   path('cargo/detalle/<int:pk>', CargoDetalle.as_view(template_name = "crud/cargo/detalle.html"), name='detallecargo'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cargo o registro  
   #path('cargo/crear', CargoCrear.as_view(template_name = "crud/cargo/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cargo registro de la Base de Datos 
   path('cargo/editar/<int:pk>', CargoActualizar.as_view(template_name = "crud/cargo/actualizar.html"), name='actualizarcargo'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cargo o registro de la Base de Datos 
   path('cargo/eliminar/<int:pk>', CargoEliminar.as_view(template_name ='crud/cargo/eliminar.html')), 

##----------------------------------------------------------Cargo---------------------------------------------------------------##


   
##-----------------------------------------------------------Cita---------------------------------------------------------------##

   path('cita/', ListadoCita.as_view(template_name = "crud/cita/tables.html"), name='leercita'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path('cita/detalle/<int:pk>', CitaDetalle.as_view(template_name = "crud/cita/detalle.html"), name='detallecita'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('cita/editar/<int:pk>', CitaActualizar.as_view(template_name = "crud/cita/actualizar.html"), name='actualizarcita'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('cita/eliminar/<int:pk>', CitaEliminar.as_view(template_name ='crud/cita/eliminar.html')), 

##----------------------------------------------------------cargo---------------------------------------------------------------##



##-----------------------------------------------------------Dia---------------------------------------------------------------##

   path('dia/', ListadoDia.as_view(template_name = "crud/dia/tables.html"), name='leerdia'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path('dia/detalle/<int:pk>', DiaDetalle.as_view(template_name = "crud/dia/detalle.html"), name='detalledia'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('dia/editar/<int:pk>', DiaActualizar.as_view(template_name = "crud/dia/actualizar.html"), name='actualizardia'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('dia/eliminar/<int:pk>', DiaEliminar.as_view(template_name ='crud/dia/eliminar.html')), 

##----------------------------------------------------------Dia---------------------------------------------------------------##



##-----------------------------------------------------------Dieta---------------------------------------------------------------##

   path('dieta/',ListadoDieta.as_view(template_name = "crud/dieta/tables.html"), name='leerdieta'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('dieta/detalle/<int:pk>', DietaDetalle.as_view(template_name = "dieta/detalle.html"), name='detalledieta'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('dieta/editar/<int:pk>', DietaActualizar.as_view(template_name = "cru/dieta/actualizar.html"), name='actualizardia'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('dieta/eliminar/<int:pk>', DietaEliminar.as_view(template_name ='crud/dieta/eliminar.html')), 

##----------------------------------------------------------Dieta---------------------------------------------------------------##



##-----------------------------------------------------------Ejercicio---------------------------------------------------------------##

   path('ejercicio/', ListadoEjercicio.as_view(template_name = "crud/ejercicio/tables.html"), name='leerejercicio'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path('ejercicio/detalle/<int:pk>', EjercicioDetalle.as_view(template_name = "ejercicio/detalle.html"), name='detalleejercicio'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('ejercicio/editar/<int:pk>',EjercicioActualizar.as_view(template_name = "cru/ejercicio/actualizar.html"), name='actualizarejercicio'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('ejercicio/eliminar/<int:pk>',EjercicioEliminar.as_view(template_name ='crud/ejercicio/eliminar.html')), 

##----------------------------------------------------------Ejercicio---------------------------------------------------------------##



##-----------------------------------------------------------Enfoque---------------------------------------------------------------##

   path('enfoque/', ListadoEnfoque.as_view(template_name = "crud/enfoque/tables.html"), name='leerenfoque'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('enfoque/detalle/<int:pk>', EnfoqueDetalle.as_view(template_name = "enfoque/detalle.html"), name='detalleenfoque'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('enfoque/editar/<int:pk>', EnfoqueActualizar.as_view(template_name = "cru/enfoque/actualizar.html"), name='actualizarenfoque'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('enfoque/eliminar/<int:pk>', EnfoqueEliminar.as_view(template_name ='crud/enfoque/eliminar.html')), 

##----------------------------------------------------------Enfoque---------------------------------------------------------------##



##-----------------------------------------------------------Enfoque---------------------------------------------------------------##

   path('enfoque/', ListadoEnfoque.as_view(template_name = "crud/enfoque/tables.html"), name='leerenfoque'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('enfoque/detalle/<int:pk>', EnfoqueDetalle.as_view(template_name = "enfoque/detalle.html"), name='detalleenfoque'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('enfoque/editar/<int:pk>', EnfoqueActualizar.as_view(template_name = "cru/enfoque/actualizar.html"), name='actualizarenfoque'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('enfoque/eliminar/<int:pk>', EnfoqueEliminar.as_view(template_name ='crud/enfoque/eliminar.html')), 

##----------------------------------------------------------Enfoque---------------------------------------------------------------##



##-----------------------------------------------------------Estado---------------------------------------------------------------##

   path('estado/', ListadoEstado.as_view(template_name = "crud/estado/tables.html"), name='leerestado'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('estado/detalle/<int:pk>', EstadoDetalle.as_view(template_name = "estado/detalle.html"), name='detalleestado'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('estado/editar/<int:pk>', EstadoActualizar.as_view(template_name = "cru/estado/actualizar.html"), name='actualizarestado'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('estado/eliminar/<int:pk>', EstadoEliminar.as_view(template_name ='crud/estado/eliminar.html')), 

##---------------------------------------------------------Estado---------------------------------------------------------------##



##-----------------------------------------------------------Evolucion---------------------------------------------------------------##

   path('evolucion/', ListadoEvolucion.as_view(template_name = "crud/evolucion/tables.html"), name='leerevolucion'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('evolucion/detalle/<int:pk>', EvolucionDetalle.as_view(template_name = "evolucion/detalle.html"), name='detalleevolucion'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('evolucion/editar/<int:pk>', EvolucionActualizar.as_view(template_name = "cru/evolucion/actualizar.html"), name='actualizarevolucion'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('evolucion/eliminar/<int:pk>', EvolucionEliminar.as_view(template_name ='crud/evolucion/eliminar.html')), 

##---------------------------------------------------------Evolucion---------------------------------------------------------------##



##-----------------------------------------------------------Genero---------------------------------------------------------------##

   path('genero/', ListadoGenero.as_view(template_name = "crud/genero/tables.html"), name='leergenero'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('genero/detalle/<int:pk>', GeneroDetalle.as_view(template_name = "genero/detalle.html"), name='detallegenero'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('genero/editar/<int:pk>', GeneroActualizar.as_view(template_name = "cru/genero/actualizar.html"), name='actualizargenero'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('genero/eliminar/<int:pk>', GeneroEliminar.as_view(template_name ='crud/genero/eliminar.html')), 

##---------------------------------------------------------Genero---------------------------------------------------------------##



##-----------------------------------------------------------Historia---------------------------------------------------------------##

   path('historia/', ListadoHistoria.as_view(template_name = "crud/historia/tables.html"), name='leerhistoria'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('historia/detalle/<int:pk>', HistoriaDetalle.as_view(template_name = "historia/detalle.html"), name='detallehistoria'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('historia/editar/<int:pk>', HistoriaActualizar.as_view(template_name = "cru/historia/actualizar.html"), name='actualizarhistoria'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('historia/eliminar/<int:pk>', HistoriaEliminar.as_view(template_name ='crud/historia/eliminar.html')), 

##---------------------------------------------------------Historia---------------------------------------------------------------##



##-----------------------------------------------------------Horario---------------------------------------------------------------##

   path('horario/', ListadoHorario.as_view(template_name = "crud/horario/tables.html"), name='leerhorario'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('horario/detalle/<int:pk>', HorarioDetalle.as_view(template_name = "horario/detalle.html"), name='detallehorario'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('horario/editar/<int:pk>', HorarioActualizar.as_view(template_name = "cru/horario/actualizar.html"), name='actualizarhorario'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('horario/eliminar/<int:pk>', HorarioEliminar.as_view(template_name ='crud/horario/eliminar.html')), 

##---------------------------------------------------------Horario---------------------------------------------------------------##



##-----------------------------------------------------------Ingrediente---------------------------------------------------------------##

   path('ingrediente/', ListadoIngrediente.as_view(template_name = "crud/ingrediente/tables.html"), name='leeringrediente'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('ingrediente/detalle/<int:pk>', IngredienteDetalle.as_view(template_name = "ingrediente/detalle.html"), name='detalleingrediente'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('ingrediente/editar/<int:pk>', IngredienteActualizar.as_view(template_name = "cru/ingrediente/actualizar.html"), name='actualizaringrediente'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('ingrediente/eliminar/<int:pk>', IngredienteEliminar.as_view(template_name ='crud/ingrediente/eliminar.html')), 

##---------------------------------------------------------Ingrediente---------------------------------------------------------------##



##-----------------------------------------------------------Medida---------------------------------------------------------------##

   path('medida/', ListadoMedida.as_view(template_name = "crud/medida/tables.html"), name='leermedida'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('medida/detalle/<int:pk>', MedidaDetalle.as_view(template_name = "medida/detalle.html"), name='detallemedida'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('medida/editar/<int:pk>', MedidaActualizar.as_view(template_name = "cru/medida/actualizar.html"), name='actualizarmedida'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('medida/eliminar/<int:pk>', MedidaEliminar.as_view(template_name ='crud/medida/eliminar.html')), 

##---------------------------------------------------------Medida------------------------------------------------------Medida



##-----------------------------------------------------------Ocupacion---------------------------------------------------------------##

   path('ocupacion/', ListadoOcupacion.as_view(template_name = "crud/ocupacion/tables.html"), name='leerocupacion'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('ocupacion/detalle/<int:pk>', OcupacionDetalle.as_view(template_name = "ocupacion/detalle.html"), name='detalleocupacion'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('ocupacion/editar/<int:pk>', OcupacionActualizar.as_view(template_name = "cru/ocupacion/actualizar.html"), name='actualizarocupacion'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('ocupacion/eliminar/<int:pk>', OcupacionEliminar.as_view(template_name ='crud/ocupacion/eliminar.html')), 

##---------------------------------------------------------Ocupacion---------------------------------------------------------------##



##-----------------------------------------------------------Persona---------------------------------------------------------------##

   path('persona/', ListadoPersona.as_view(template_name = "crud/persona/tables.html"), name='leerpersona'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('persona/detalle/<int:pk>', PersonaDetalle.as_view(template_name = "persona/detalle.html"), name='detallepersona'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "cru/persona/actualizar.html"), name='actualizarpersona'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('persona/eliminar/<int:pk>', PersonaEliminar.as_view(template_name ='crud/persona/eliminar.html')), 

##---------------------------------------------------------Persona---------------------------------------------------------------##



##-----------------------------------------------------------Plan---------------------------------------------------------------##

   path('plan/', ListadoPlan.as_view(template_name = "crud/plan/tables.html"), name='leerplan'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('plan/detalle/<int:pk>', PlanDetalle.as_view(template_name = "plan/detalle.html"), name='detalleplan'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('plan/editar/<int:pk>', PlanActualizar.as_view(template_name = "cru/plan/actualizar.html"), name='actualizarplan'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('plan/eliminar/<int:pk>', PlanEliminar.as_view(template_name ='crud/plan/eliminar.html')), 

##---------------------------------------------------------Plan---------------------------------------------------------------##



##-----------------------------------------------------------Planificacion---------------------------------------------------------------##

   path('planificacion/', ListadoPlanificacion.as_view(template_name = "crud/planificacion/tables.html"), name='leerplanificacion'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('planificacion/detalle/<int:pk>', PlanificacionDetalle.as_view(template_name = "planificacion/detalle.html"), name='detalleplanificacion'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('planificacion/editar/<int:pk>', PlanificacionActualizar.as_view(template_name = "cru/planificacion/actualizar.html"), name='actualizarplanificacion'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('planificacion/eliminar/<int:pk>', PlanificacionEliminar.as_view(template_name ='crud/planificacion/eliminar.html')), 

##---------------------------------------------------------Planificacion---------------------------------------------------------------##



##-----------------------------------------------------------Receta---------------------------------------------------------------##

   path('receta/', ListadoReceta.as_view(template_name = "crud/receta/tables.html"), name='leerreceta'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('receta/detalle/<int:pk>', RecetaDetalle.as_view(template_name = "receta/detalle.html"), name='detallereceta'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('receta/editar/<int:pk>', RecetaActualizar.as_view(template_name = "cru/receta/actualizar.html"), name='actualizarreceta'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('receta/eliminar/<int:pk>', RecetaEliminar.as_view(template_name ='crud/receta/eliminar.html')), 

##---------------------------------------------------------Receta---------------------------------------------------------------##



##-----------------------------------------------------------Repeticion---------------------------------------------------------------##

   path('repeticion/', ListadoRepeticion.as_view(template_name = "crud/repeticion/tables.html"), name='leerrepeticion'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('repeticion/detalle/<int:pk>', RepeticionDetalle.as_view(template_name = "repeticion/detalle.html"), name='detallerepeticion'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('repeticion/editar/<int:pk>', RepeticionActualizar.as_view(template_name = "cru/repeticion/actualizar.html"), name='actualizarrepeticion'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('repeticion/eliminar/<int:pk>', RepeticionEliminar.as_view(template_name ='crud/repeticion/eliminar.html')), 

##---------------------------------------------------------Repeticion---------------------------------------------------------------##



##-----------------------------------------------------------Rutina---------------------------------------------------------------##

   path('rutina/', ListadoRutina.as_view(template_name = "crud/rutina/tables.html"), name='leerrutina'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('rutina/detalle/<int:pk>', RutinaDetalle.as_view(template_name = "rutina/detalle.html"), name='detallerutina'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('rutina/editar/<int:pk>', RutinaActualizar.as_view(template_name = "cru/rutina/actualizar.html"), name='actualizarrutina'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('rutina/eliminar/<int:pk>', RutinaEliminar.as_view(template_name ='crud/rutina/eliminar.html')), 

##---------------------------------------------------------Rutina------------------------------------------------------------##



##-----------------------------------------------------------Serie---------------------------------------------------------------##

   path('rutina/', ListadoSerie.as_view(template_name = "crud/rutina/tables.html"), name='leerrutina'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('rutina/detalle/<int:pk>', SerieDetalle.as_view(template_name = "rutina/detalle.html"), name='detallerutina'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('rutina/editar/<int:pk>', SerieActualizar.as_view(template_name = "cru/rutina/actualizar.html"), name='actualizarrutina'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('rutina/eliminar/<int:pk>', SerieEliminar.as_view(template_name ='crud/rutina/eliminar.html')), 

##---------------------------------------------------------Serie------------------------------------------------------------##



##-----------------------------------------------------------Tipocomida---------------------------------------------------------------##

   path('tipocomida/', ListadoTipocomida.as_view(template_name = "crud/tipocomida/tables.html"), name='leertipocomida'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('tipocomida/detalle/<int:pk>', TipocomidaDetalle.as_view(template_name = "tipocomida/detalle.html"), name='detalletipocomida'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('tipocomida/editar/<int:pk>', TipocomidaActualizar.as_view(template_name = "cru/tipocomida/actualizar.html"), name='actualizartipocomida'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('tipocomida/eliminar/<int:pk>', TipocomidaEliminar.as_view(template_name ='crud/tipocomida/eliminar.html')), 

##---------------------------------------------------------Tipocomida------------------------------------------------------------##



##-----------------------------------------------------------Tipodocumento---------------------------------------------------------------##

   path('tipodocumento/', ListadoTipodocumento.as_view(template_name = "crud/tipodocumento/tables.html"), name='leertipodocumento'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('tipodocumento/detalle/<int:pk>', TipodocumentoDetalle.as_view(template_name = "tipodocumento/detalle.html"), name='detalletipodocumento'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('tipodocumento/editar/<int:pk>', TipodocumentoActualizar.as_view(template_name = "cru/tipodocumento/actualizar.html"), name='actualizartipodocumento'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('tipodocumento/eliminar/<int:pk>', TipodocumentoEliminar.as_view(template_name ='crud/tipodocumento/eliminar.html')), 

##---------------------------------------------------------Tipodocumento------------------------------------------------------------##



##-----------------------------------------------------------Tipopersona---------------------------------------------------------------##

   path('tipopersona/', ListadoTipopersona.as_view(template_name = "crud/tipopersona/tables.html"), name='leertipopersona'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('tipopersona/detalle/<int:pk>', TipopersonaDetalle.as_view(template_name = "tipopersona/detalle.html"), name='detalletipopersona'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('tipopersona/editar/<int:pk>', TipopersonaActualizar.as_view(template_name = "cru/tipopersona/actualizar.html"), name='actualizartipopersona'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('tipopersona/eliminar/<int:pk>', TipopersonaEliminar.as_view(template_name ='crud/tipopersona/eliminar.html')), 

##---------------------------------------------------------Tipopersona------------------------------------------------------------##



##-----------------------------------------------------------Tipoplan---------------------------------------------------------------##

   path('tipoplan/', ListadoTipoplan.as_view(template_name = "crud/tipoplan/tables.html"), name='leertipoplan'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('tipoplan/detalle/<int:pk>', TipoplanDetalle.as_view(template_name = "tipoplan/detalle.html"), name='detalletipoplan'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('tipoplan/editar/<int:pk>', TipoplanActualizar.as_view(template_name = "cru/tipoplan/actualizar.html"), name='actualizartipoplan'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('tipoplan/eliminar/<int:pk>', TipoplanEliminar.as_view(template_name ='crud/tipoplan/eliminar.html')), 

##---------------------------------------------------------Tipoplan------------------------------------------------------------##



##-----------------------------------------------------------Tipoalimento---------------------------------------------------------------##

   path('tipoalimento/', ListadoTipoalimento.as_view(template_name = "crud/tipoalimento/tables.html"), name='leertipoalimento'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('tipoalimento/detalle/<int:pk>', TipoalimentoDetalle.as_view(template_name = "tipoalimento/detalle.html"), name='detalletipoalimento'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('tipoalimento/editar/<int:pk>', TipoalimentoActualizar.as_view(template_name = "cru/tipoalimento/actualizar.html"), name='actualizartipoalimento'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('tipoalimento/eliminar/<int:pk>', TipoalimentoEliminar.as_view(template_name ='crud/tipoalimento/eliminar.html')), 

##---------------------------------------------------------Tipoalimento------------------------------------------------------------##



##-----------------------------------------------------------Usuario---------------------------------------------------------------##

   path('usuario/', ListadoUsuario.as_view(template_name = "crud/usuario/tables.html"), name='leerusuario'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   path ('usuario/detalle/<int:pk>', UsuarioDetalle.as_view(template_name = "usuario/detalle.html"), name='detalleusuario'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   path('usuario/editar/<int:pk>', UsuarioActualizar.as_view(template_name = "cru/usuario/actualizar.html"), name='actualizarusuario'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   path('usuario/eliminar/<int:pk>', UsuarioEliminar.as_view(template_name ='crud/usuario/eliminar.html')), 

##---------------------------------------------------------Usuario------------------------------------------------------------##

##-----------------------------------------------------------ZZZZZ---------------------------------------------------------------##

   #path('zzz/', ListadoZZZZZ.as_view(template_name = "crud/zzz/tables.html"), name='leerzzz'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Cita registro 
   #path ('zzz/detalle/<int:pk>', ZZZZZDetalle.as_view(template_name = "zzz/detalle.html"), name='detallezzz'),

   # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo Cita o registro  
   #path('cita/crear', CitaCrear.as_view(template_name = "crud/cita/crear.html"), name='crear'),
     
   # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cita registro de la Base de Datos 
   #path('zzz/editar/<int:pk>', ZZZZZActualizar.as_view(template_name = "cru/zzz/actualizar.html"), name='actualizarzzz'), 

   # La ruta 'eliminar' que usaremos para eliminar un Cita o registro de la Base de Datos 
   #path('zzz/eliminar/<int:pk>', ZZZZZEliminar.as_view(template_name ='crud/zzz/eliminar.html')), 

##---------------------------------------------------------ZZZZZ------------------------------------------------------------##



                                                         ## Fin De Crud ##



 ##-----------------------------------------------------------Catalogo------------------------------------------------------------##

   path('catalogo/', ListadoTipoplan.as_view(template_name = 'CATALOGO/catalogo.html'), name='leercatalogo'),
   path('catalogo/', ListadoTipoplan.as_view(template_name = 'CATALOGO/tables.html'), name='crearplan'),
  
   # La ruta 'detalles' en donde mostraremos una página con los detalles de un Plan registro 
   path('catalogo/detalle/<int:pk>', TipoplanDetalle.as_view(template_name = 'CATALOGO/detalle.html'), name='detalleplan'),

 ##-----------------------------------------------------------Catalogo------------------------------------------------------------##

]
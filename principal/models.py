# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cargo(models.Model):
    idcargo = models.IntegerField(primary_key=True, db_comment='sirve para identificar la tabla de cargo ')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el nombre del cargo ')

    class Meta:
        managed = False
        db_table = 'cargo'
        db_table_comment = 'esta tabla sirve para guardar todos loa cargos'


class Cita(models.Model):
    idcita = models.IntegerField(primary_key=True)
    horacita = models.IntegerField(blank=True, null=True, db_comment='sirve para guardar la hora de la cita ')
    fecha = models.IntegerField(blank=True, null=True, db_comment='sirve para guardar la fecha de la cita ')
    notas = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar las notas de la cita')
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_idpersona', db_comment='sirve para guardar a las personas que solicitaron una cita ')
    estado_idestado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado_idestado', db_comment='sirve para guardar el estado de la cita')

    class Meta:
        managed = False
        db_table = 'cita'
        db_table_comment = 'sirve para guardar las citas '


class Dia(models.Model):
    iddia = models.IntegerField(primary_key=True)
    dia = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dia'


class Dieta(models.Model):
    iddieta = models.IntegerField(primary_key=True)
    idempleado = models.CharField(max_length=45, blank=True, null=True)
    planificacion_idplanificacion = models.ForeignKey('Planificacion', models.DO_NOTHING, db_column='planificacion_idplanificacion')
    receta_idreceta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='receta_idreceta')

    class Meta:
        managed = False
        db_table = 'dieta'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ejercicio(models.Model):
    idejercicio = models.IntegerField(primary_key=True, db_comment='sirve para identificar la tabla de los ejercicios ')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el nombre de los ejercicios ')
    imagen = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar las imagenes de los ejercicios ')

    class Meta:
        managed = False
        db_table = 'ejercicio'
        db_table_comment = 'sirve para guardar los ejercisios '


class Enfoque(models.Model):
    idenfoque = models.IntegerField(primary_key=True, db_comment='sirve para identificar la tabla de enfoques ')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el nombre del enfoque ')

    class Meta:
        managed = False
        db_table = 'enfoque'
        db_table_comment = 'sirve para  guardar los enfoques de las personas'


class Estado(models.Model):
    idestado = models.IntegerField(primary_key=True, db_comment='sirve para identificar la tabla de estado')
    estado = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar los estados ')

    class Meta:
        managed = False
        db_table = 'estado'
        db_table_comment = 'esta tabla guarda los estados '


class Evolucion(models.Model):
    idevolucion = models.IntegerField(primary_key=True, db_comment='sirve para identificar la tabla de evoluciones ')
    medida_idmedida = models.ForeignKey('Medida', models.DO_NOTHING, db_column='medida_idmedida', db_comment='sirven para guardar las medidas de las personas ')
    rutina_idrutina = models.ForeignKey('Rutina', models.DO_NOTHING, db_column='rutina_idrutina', db_comment='sirve para guardar las rutoinas de las personas ')
    dieta_iddieta = models.ForeignKey(Dieta, models.DO_NOTHING, db_column='dieta_iddieta', db_comment='sirve para guardar las dietas de las personas ')
    fecha = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar las fechas de las evoluciones ')

    class Meta:
        managed = False
        db_table = 'evolucion'
        db_table_comment = 'sirve para guardar las evoluciones '


class Genero(models.Model):
    idgenero = models.IntegerField(primary_key=True, db_comment='este campo nos ayuda a registrar los generos')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='este campo nos ayuda a distinguir los generos ')

    class Meta:
        managed = False
        db_table = 'genero'
        db_table_comment = 'esta tabla ayuda a guardar los generos'


class Historia(models.Model):
    idhistoria = models.IntegerField(primary_key=True, db_comment='nos ayuda a ver como esta de salud la persona')
    evolucion_idevolucion = models.ForeignKey(Evolucion, models.DO_NOTHING, db_column='evolucion_idevolucion', db_comment='nos ayuda a ver los diferentes cambios en la persona')

    class Meta:
        managed = False
        db_table = 'historia'
        db_table_comment = 'esta sirve para registrar los diferentes estpas de la persona'


class Horario(models.Model):
    idhorario = models.IntegerField(primary_key=True, db_comment='sirve para identificar las tablas de las personas ')
    fecha = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar la fecha de los horarios ')
    horainicio = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar la hora de inicio ')
    horafin = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardarla hora final del horario ')
    cita_idcita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='cita_idcita', db_comment='sirve para guardar las citas')

    class Meta:
        managed = False
        db_table = 'horario'
        db_table_comment = 'sirve para guardar los horarios '


class Ingrediente(models.Model):
    idingrediente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el nombre de los ingredientes ')
    racion = models.IntegerField(db_comment='sirve para guardar la racion de los alimentos ')
    ingredientescol = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el ingrediente')
    proteinas = models.FloatField(blank=True, null=True, db_comment='sirve para guardar las proteinas de los alimentos')
    carbohidratos = models.FloatField(blank=True, null=True, db_comment='irven para guardar los carbohidratos de los alimentos ')
    calorias = models.FloatField(blank=True, null=True, db_comment='sirve para guardar las calorias de los alimentos ')
    grasas = models.FloatField(blank=True, null=True, db_comment='sirve para guardar la grasa de los alimentos ')

    class Meta:
        managed = False
        db_table = 'ingrediente'
        db_table_comment = 'sirve para guardar los ingredientes '


class Medida(models.Model):
    idmedida = models.IntegerField(primary_key=True, db_comment='sirve para darle una identidad a la tabla')
    estatura = models.FloatField(blank=True, null=True, db_comment='sirve para tener unas medidas de la persona')
    peso = models.FloatField(blank=True, null=True, db_comment='sirve para guardar los  diferentes pesos')
    indicegrasa = models.IntegerField(blank=True, null=True, db_comment='sirve para guardar todos los indiices de grasas en las personas')
    imc = models.FloatField(db_column='IMC', blank=True, null=True, db_comment='sirve para guardar todos los imc de las personas ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medida'
        db_table_comment = 'sirve para registrar todas las medidas de los usuarios '


class Metodopago(models.Model):
    idmetodopago = models.IntegerField(primary_key=True, db_comment='sirve para identificar la tabla de metdo de pago')
    metodo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metodopago'


class Ocupacion(models.Model):
    idocupacion = models.IntegerField(primary_key=True, db_comment='sirve para identificar las tabla de ocupacion ')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para distinguir los cargos y guardarlos ')

    class Meta:
        managed = False
        db_table = 'ocupacion'
        db_table_comment = 'sirve para guardar las ocupaciones '


class Pago(models.Model):
    idpago = models.IntegerField(primary_key=True, db_comment='sirve para registrar la tabla de pagos')
    fechapago = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar la fecha de pagos')
    montopagado = models.FloatField(blank=True, null=True, db_comment='sirve para guardar el monto de los pagos')

    class Meta:
        managed = False
        db_table = 'pago'


class Pagos(models.Model):
    idpago = models.IntegerField(primary_key=True, db_comment='sirve para identificar las tablas de pagos ')

    class Meta:
        managed = False
        db_table = 'pagos'


class Persona(models.Model):
    idpersona = models.IntegerField(primary_key=True, db_comment='sirve par identificar mas facilmente la tabla')
    nombre1 = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el primer nombre ')
    nombre2 = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el segundo nombre de la persona ')
    apellido1 = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el primer apellido ')
    apellido2 = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el segundo apellido de la persona')
    numid = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para registrar a las personas ')
    edad = models.IntegerField(blank=True, null=True, db_comment='sirve para guarda la edad de las personas ')
    email = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar  el contacto de las personas')
    celular = models.IntegerField(blank=True, null=True, db_comment='sirve para tener un registro del contacto de las personas ')
    direccion = models.IntegerField(blank=True, null=True, db_comment='sirve para guardar la direccion de las personas ')
    genero_idgenero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='genero_idgenero', db_comment='sirve para identificar la tabla de genero ')
    tipodocumento_idtipodocumento = models.ForeignKey('Tipodocumento', models.DO_NOTHING, db_column='tipodocumento_idtipodocumento', db_comment='sirve para identificar la tabla')
    cargo_idcargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='cargo_idcargo', db_comment='sirve para identificar la tabla')
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_idusuario', db_comment='sirve para identificar la tabla de usuarios')
    tipopersona_idtipopersona = models.ForeignKey('Tipopersona', models.DO_NOTHING, db_column='tipopersona_idtipopersona', db_comment='sirve para identificar la tabla de tipo de persona ')
    ocupacion_idocupacion = models.ForeignKey(Ocupacion, models.DO_NOTHING, db_column='ocupacion_idocupacion', db_comment='sirve para identificar la tabla de ocupacion ')
    plan_idmembresia = models.ForeignKey('Plan', models.DO_NOTHING, db_column='plan_idmembresia', db_comment='sirve para identificar la tabla de membresia')
    historia_idhistoria = models.ForeignKey(Historia, models.DO_NOTHING, db_column='historia_idhistoria', db_comment='sirve para identificar la tabla de historia ')

    class Meta:
        managed = False
        db_table = 'persona'
        db_table_comment = 'esta tabla registra a las personas ademas almacena los datos'


class Plan(models.Model):
    idmembresia = models.IntegerField(primary_key=True, db_comment='sirve para identificar la tabla de membresia ')
    fechainicio = models.DateField(blank=True, null=True, db_comment='sirve par guardar la fecha de inicio ')
    fechafin = models.DateField(blank=True, null=True, db_comment='sirve para guardar la fecha del fin')
    tipoplan_idtipoplan = models.ForeignKey('Tipoplan', models.DO_NOTHING, db_column='tipoplan_idtipoplan', db_comment='sirve para guardar el plan que escoge la persona ')
    foto = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'plan'
        db_table_comment = 'sirve para guardar los planes que hay en el gimnasio '


class Planificacion(models.Model):
    idplanificacion = models.IntegerField(primary_key=True, db_comment='sirve para identificar la tabla de planificacion ')
    cantidad = models.IntegerField(blank=True, null=True, db_comment='sirve para guardar la cantidad indicada ')

    class Meta:
        managed = False
        db_table = 'planificacion'
        db_table_comment = 'sirve para guardar las planificaciones de cada persona '


class Receta(models.Model):
    idreceta = models.IntegerField(primary_key=True, db_comment='sirve para identificar la tabla de recetas ')
    imagen = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar las imagenes de las recetas ')
    preparacion = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar las preparaciones de las recetas ')
    carbohidratos = models.FloatField(blank=True, null=True, db_comment='sirve para guardar las ganancias de carbohidratos en el cuerpo')
    calorias = models.FloatField(db_comment='sirve para guardar el registro de calorias de cada alimento')
    grasas = models.FloatField(blank=True, null=True, db_comment='sirve para guardar el indice de grasas de cada alimento')
    tipoalimento_idtipoalimento = models.ForeignKey('Tipoalimento', models.DO_NOTHING, db_column='tipoalimento_idtipoalimento')

    class Meta:
        managed = False
        db_table = 'receta'


class Repeticion(models.Model):
    idrepeticion = models.IntegerField(primary_key=True)
    cantidad = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repeticion'


class Rutina(models.Model):
    idrutina = models.IntegerField(primary_key=True)
    dia_iddia = models.ForeignKey(Dia, models.DO_NOTHING, db_column='dia_iddia', db_comment='sirve para guardar el dia de las rutinas ')
    ejercicio_idejercicio = models.ForeignKey(Ejercicio, models.DO_NOTHING, db_column='ejercicio_idejercicio', db_comment='sirve para guardar la rutina de ejercicios ')
    serie_idserie = models.ForeignKey('Serie', models.DO_NOTHING, db_column='serie_idserie', db_comment='sirve para guardar la serie de ejercicios ')
    repeticion_idrepeticion = models.ForeignKey(Repeticion, models.DO_NOTHING, db_column='repeticion_idrepeticion', db_comment='sirve para guardar las repeticione de los ejercisios ')

    class Meta:
        managed = False
        db_table = 'rutina'
        db_table_comment = 'sirve para guardar las rutinas '


class Serie(models.Model):
    idserie = models.IntegerField(primary_key=True, db_comment='sirve para identificar la tabla de series ')
    cantidad = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardarr la cantidad de las series ')

    class Meta:
        managed = False
        db_table = 'serie'
        db_table_comment = 'sirve para guardar las series de los ejercicios'


class Tipoalimento(models.Model):
    idtipoalimento = models.IntegerField(primary_key=True, db_comment='sirve para identificar la tabla de tipo de alimento')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el nombre de los tipos de alimentos')
    descripcion = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para dar una informacion pequeña de los productos ')
    verduras = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve como tipo de alimentos')
    granos = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve como tipo de alimentos')
    ensaladas = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve como tipo de alimentos')
    bebidas = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve como tipo de bebidas')
    frutas = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve como tipo de frutas')
    ingrediente_idingrediente = models.ForeignKey(Ingrediente, models.DO_NOTHING, db_column='ingrediente_idingrediente', db_comment='sirve para guardar los ingredientes ')

    class Meta:
        managed = False
        db_table = 'tipoalimento'
        db_table_comment = 'sirve guardar el tipo de alimentos '


class Tipocomida(models.Model):
    idtipocomida = models.IntegerField(primary_key=True, db_comment='sirve para identificar la tabla de comidas ')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el nombre de las comidas ')
    descripcion = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para dar una pequeña informacion de la comida ')
    desayuno = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar las comidas que sean de desayuno')
    almuerzo = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar las comidas que sean del almuerzo ')
    mediatarde = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar las comidas que se comen en la tarde ')
    cena = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar las comidas que se sirven en la noche ')
    entrenoche = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar las comidas que se sirvan en la noche ')
    ingrediente_idingrediente = models.ForeignKey(Ingrediente, models.DO_NOTHING, db_column='ingrediente_idingrediente', db_comment='sirve para guardar los ingredientes ')

    class Meta:
        managed = False
        db_table = 'tipocomida'
        db_table_comment = 'sirve para guardar los diferentes tipos de comidas '


class Tipodocumento(models.Model):
    idtipodocumento = models.IntegerField(primary_key=True, db_comment='sirve para indentificar la tabla de documento')
    tipodoc = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el tipo de documento que tiene la persona ')

    class Meta:
        managed = False
        db_table = 'tipodocumento'
        db_table_comment = 'sirve para guardar el documento de las personas '


class Tipopersona(models.Model):
    idtipopersona = models.IntegerField(primary_key=True, db_comment='sirve para identificar la tabla de tipo de persona ')
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el nombre del tipo de la persona')

    class Meta:
        managed = False
        db_table = 'tipopersona'


class Tipoplan(models.Model):
    idtipoplan = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el nombre de los planes')
    precio = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar el precio de los planes ')

    class Meta:
        managed = False
        db_table = 'tipoplan'
        db_table_comment = 'sirve para guardar los tipos de planes que hay en el gimnasio '


class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True, db_comment='nos sirve para guardar el nombre de la persona ')
    clave = models.CharField(max_length=45, blank=True, null=True, db_comment='sirve para guardar las claves de las personas y asi agregarle seguridad')

    class Meta:
        managed = False
        db_table = 'usuario'
        db_table_comment = 'sirve para guardar los datos de usarios '

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class Asegurado(models.Model):
    rut_asegurado = models.CharField(
        primary_key=True, max_length=10, verbose_name='Rut')
    primer_nombre = models.CharField(
        max_length=20, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(
        max_length=20, verbose_name='Segundo Nombre')
    primer_apellido = models.CharField(
        max_length=20, verbose_name='Apellido Paterno')
    segundo_apeliido = models.CharField(
        max_length=20, verbose_name='Apellido Materno')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    telefono = models.CharField(verbose_name='Teléfono', max_length=9)
    fecha_nacimiento = models.DateField(verbose_name='Fecha Nacimiento')
    estado = models.CharField(max_length=1, default=1)
    direccion = models.CharField(
        max_length=150, verbose_name='Dirección asegurado')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    comuna_id_comuna = models.ForeignKey(
        'Comuna', models.DO_NOTHING, db_column='comuna_id_comuna', verbose_name='Comuna', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'asegurado'
    #     verbose_name_plural = 'Asegurados'

    def __str__(self):
        return self.rut_asegurado


class Comuna(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    region_nro_region = models.ForeignKey(
        'Region', models.DO_NOTHING, db_column='region_nro_region', verbose_name='Región', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'comuna'
    #     verbose_name_plural = 'Comuna'

    def __str__(self):
        return self.nombre


class EstadoPresupuesto(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')

    # class Meta:
    #     managed = False
    #     db_table = 'estado_presupuesto'
    #     verbose_name_plural = 'Estado Presupuestos'

    def __str__(self):
        return self.nombre


class EstadoSiniestro(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')

    # class Meta:
    #     managed = False
    #     db_table = 'estado_siniestro'
    #     verbose_name_plural = 'Estado Siniestros'

    def __str__(self):
        return str(self.nombre)


class FormularioActa(models.Model):
    fecha_hora = models.DateField(verbose_name='Fecha', auto_now=True)
    observaciones = models.CharField(
        max_length=300, blank=True, null=True, verbose_name='Observaciones')
    tipo_acta_id_tipo_acta = models.ForeignKey(
        'TipoActa', models.DO_NOTHING, db_column='tipo_acta_id_tipo_acta', verbose_name='Tipo Acta', null=True)
    siniestro_id = models.ForeignKey(
        'Siniestro', models.DO_NOTHING, db_column='siniestro_id', verbose_name='ID Siniestro', null=True)
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller', null=True)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'formulario_acta'
    #     verbose_name_plural = 'Formulario Actas'

    # def __str__(self):
    #     return str(self.fecha_hora)


class Grua(models.Model):
    patente_grua = models.CharField(
        primary_key=True, max_length=10, verbose_name='Patente Grúa')
    estado = models.CharField(max_length=1, verbose_name='Estado', default=1)
    estado_delete = models.CharField(
        max_length=1, verbose_name='Estado delete', default=1)
    servicio_grua_id_servicio = models.ForeignKey(
        'ServicioGrua', models.DO_NOTHING, db_column='servicio_grua_id_servicio', verbose_name='Servicio Grúa', null=True)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'grua'
    #     verbose_name_plural = 'Grúas'

    def __str__(self):
        return self.patente_grua


class InformeDano(models.Model):
    fecha_hora = models.DateField(verbose_name='Fecha', auto_now=True)
    observaciones = models.CharField(
        max_length=1024, verbose_name='Observaciones')
    perdida_total = models.BooleanField(null=True,blank=True)
    tipo_dano_id_tipo_dano = models.ForeignKey(
        'TipoDano', models.DO_NOTHING, db_column='tipo_dano_id_tipo_dano', verbose_name='Tipo Daño', null=True)
    severidad_dano_id_seve_dano = models.ForeignKey(
        'SeveridadDano', models.DO_NOTHING, db_column='severidad_dano_id_seve_dano', verbose_name='Severidad Daño', null=True)
    vehiculo_patente_vehiculo = models.ForeignKey(
        'Vehiculo', models.DO_NOTHING, db_column='vehiculo_patente_vehiculo', verbose_name='Patente Vehículo', null=True)
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller', null=True)
    siniestro_id = models.ForeignKey(
        'Siniestro', models.DO_NOTHING, db_column='siniestro_id', verbose_name='ID Siniestro', null=True)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)

    def total(self):
        total = (self.tipo_dano_id_tipo_dano.valor + self.tipo_dano_id_tipo_dano.mano_obra) * self.severidad_dano_id_seve_dano.valor
        return total

    # class Meta:
    #     managed = False
    #     db_table = 'informe_dano'
    #     verbose_name_plural = 'Informe Daños'

    # def __str__(self):
    #     return str(self.id_info_dano)


class Marca(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre Marca')

    # class Meta:
    #     managed = False
    #     db_table = 'marca'

    def __str__(self):
        return str(self.nombre)


class Poliza(models.Model):
    vigente = models.CharField(
        max_length=1, verbose_name='Vigencia', default=1)
    fecha_inicio = models.DateField(verbose_name='Fecha Inicio')
    fecha_fin = models.DateField(verbose_name='Fecha Termino')
    estado = models.CharField(max_length=1, default=1)
    asegurado_rut_asegurado = models.ForeignKey(
        'Asegurado', models.DO_NOTHING, db_column='asegurado_rut_asegurado', verbose_name='Rut Asegurado', null=True)
    vehiculo_patente_vehiculo = models.ForeignKey(
        'Vehiculo', models.DO_NOTHING, db_column='vehiculo_patente_vehiculo', verbose_name='Patente Vehículo', null=True)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    tipo_plan_id_tip_plan = models.ForeignKey(
        'TipoPlan', models.DO_NOTHING, db_column='tipo_plan_id_tip_plan', verbose_name='Tipo plan', null=True)

    def __str__(self):
        return str(self.id)


class Presupuesto(models.Model):
    fecha_hora = models.DateField(verbose_name='Fecha')
    valor_total = models.IntegerField(verbose_name='Valor Total')
    estado_id_est_presupuesto = models.ForeignKey(
        'EstadoPresupuesto', models.DO_NOTHING, db_column='estado_id_est_presupuesto', verbose_name='ID Est. Presupuesto', null=True)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', blank=True, null=True, verbose_name='Rut Usuario')
    informe_dano_id_info_dano = models.ForeignKey(
        'InformeDano', models.DO_NOTHING, db_column='informe_dano_id_info_dano', verbose_name='ID Inf. Daño', null=True)
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'presupuesto'
    #     verbose_name_plural = 'Presupuestos'

    # def __str__(self):
    #     return str(self.id_presupuesto) + ' ' + str(self.valor_total)


class RegAsegurado(models.Model):
    nombre_asegurado = models.CharField(max_length=100)
    fecha_hora = models.DateField()
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    accion = models.CharField(max_length=50)

    # class Meta:
    #     managed = False
    #     db_table = 'reg_asegurado'


class RegError(models.Model):
    error = models.CharField(max_length=50)
    cod_error = models.CharField(max_length=500)
    mensaje = models.CharField(max_length=300)
    fecha_hora = models.DateField()

    # class Meta:
    #     managed = False
    #     db_table = 'reg_error'


class RegActas(models.Model):
    tipo_acta_id_tipo_acta = models.ForeignKey(
        'TipoActa', models.DO_NOTHING, db_column='tipo_acta_id_tipo_acta', verbose_name='Tipo Acta', null=True)
    fecha_hora = models.DateField()
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    accion = models.CharField(max_length=50)
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller', blank=True, null=True)


class RegGrua(models.Model):
    patente_grua = models.CharField(max_length=10)
    fecha_hora = models.DateField()
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    accion = models.CharField(max_length=50)

    # class Meta:
    #     managed = False
    #     db_table = 'reg_grua'


class RegInformeDano(models.Model):
    id_informe = models.IntegerField()
    fecha_hora = models.DateField()
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    accion = models.CharField(max_length=50)
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller', blank=True, null=True)


class RegPoliza(models.Model):
    nro_poliza = models.IntegerField()
    fecha_hora = models.DateField()
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    accion = models.CharField(max_length=50)

    # class Meta:
    #     managed = False
    #     db_table = 'reg_poliza'


class RegPresupuesto(models.Model):
    nro_presupuesto = models.IntegerField()
    fecha_hora = models.DateField()
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    accion = models.CharField(max_length=50)
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller', blank=True, null=True)


class RegSiniestro(models.Model):
    fecha_hora = models.DateField()
    id_siniestro = models.IntegerField()
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    accion = models.CharField(max_length=50)
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller', blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'reg_siniestro'


class RegTaller(models.Model):
    nombre_taller = models.CharField(max_length=30)
    fecha_hora = models.DateField()
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    accion = models.CharField(max_length=50)

    # class Meta:
    #     managed = False
    #     db_table = 'reg_taller'


class RegTipoPlan(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_hora = models.DateField()
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    accion = models.CharField(max_length=50)


class RegUsuario(models.Model):
    nombre_registrado = models.CharField(max_length=100)
    fecha_hora = models.DateField()
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    accion = models.CharField(max_length=50)

    # class Meta:
    #     managed = False
    #     db_table = 'reg_usuario'


class RegVehiculo(models.Model):
    patente_vehiculo = models.CharField(max_length=30)
    fecha_hora = models.DateField()
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    accion = models.CharField(max_length=50)


class Region(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre Región')

    # class Meta:
    #     managed = False
    #     db_table = 'region'
    #     verbose_name_plural = 'Regiones'

    def __str__(self):
        return self.nombre


class ServicioGrua(models.Model):
    nombre = models.CharField(max_length=400, verbose_name='Nombre')
    razon_social = models.CharField(max_length=50, verbose_name='Razón Social')
    telefono = models.BigIntegerField(verbose_name='Teléfono')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'servicio_grua'
    #     verbose_name_plural = 'Servicios Grúas'

    def __str__(self):
        return self.nombre


class SeveridadDano(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre ')
    valor = models.IntegerField(verbose_name='Valor')

    # class Meta:
    #     managed = False
    #     db_table = 'severidad_dano'
    #     verbose_name_plural = 'Severidad Daños'

    def __str__(self):
        return self.nombre


class Siniestro(models.Model):
    fecha_hr = models.DateField(verbose_name='Fecha Siniestro', auto_now=True)
    descripcion = models.CharField(max_length=1024, verbose_name='Descripción')
    parte_policial = models.ImageField(
        upload_to='partes_policiales', null=True, blank=True)
    foto_licencia = models.ImageField(
        upload_to='licencias', null=True, blank=True)
    direccion = models.CharField(
        max_length=150, verbose_name='Dirección siniestro')
    tipo_accidente_id_tipo_acc = models.ForeignKey(
        'TipoAccidente', models.DO_NOTHING, db_column='tipo_accidente_id_tipo_acc', verbose_name='Tipo Accidente', null=True)
    est_siniestro_id_est_siniestro = models.ForeignKey(
        'EstadoSiniestro', models.DO_NOTHING, db_column='est_siniestro_id_est_siniestro', verbose_name='Estado Siniestro', default=1, null=True)
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller', null=True)
    grua_patente_grua = models.ForeignKey(
        'Grua', models.DO_NOTHING, db_column='grua_patente_grua', blank=True, null=True, verbose_name='Patente Grúa')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    poliza_id_poliza = models.ForeignKey(
        'Poliza', models.DO_NOTHING, db_column='poliza_id_poliza', verbose_name='ID Póliza', null=True)
    asegurado_rut_asegurado = models.ForeignKey(
        'Asegurado', models.DO_NOTHING, db_column='asegurado_rut_asegurado', verbose_name='Rut Asegurado', null=True)
    comuna_id_comuna = models.ForeignKey(
        'Comuna', models.DO_NOTHING, db_column='comuna_id_comuna', verbose_name='Comuna', null=True)
    # class Meta:
    #     managed = False
    #     db_table = 'siniestro'
    #     verbose_name_plural = 'Siniestros'

    def __str__(self):
        return str(self.id)


class Taller(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre Taller')
    razon_social = models.CharField(max_length=50, verbose_name='Razón Social')
    telefono = models.CharField(verbose_name='Teléfono', max_length=9)
    correo = models.CharField(max_length=30, verbose_name='Correo')
    capacidad_taller = models.CharField(
        verbose_name='Capacidad Taller', max_length=3)
    estado = models.CharField(max_length=1, verbose_name='Estado', default=1)
    estado_delete = models.CharField(max_length=1, default=1)
    direccion = models.CharField(
        max_length=150, verbose_name='Dirección taller')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    comuna_id_comuna = models.ForeignKey(
        'Comuna', models.DO_NOTHING, db_column='comuna_id_comuna', verbose_name='Comuna', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'taller'
    #     verbose_name_plural = 'Talleres'

    def __str__(self):
        return self.nombre


class TipoAccidente(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')

    # class Meta:
    #     managed = False
    #     db_table = 'tipo_accidente'
    #     verbose_name_plural = 'Tipo Accidentes'

    def __str__(self):
        return self.nombre


class TipoActa(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Nombre')

    # class Meta:
    #     managed = False
    #     db_table = 'tipo_acta'
    #     verbose_name_plural = 'Tipo Actas'

    def __str__(self):
        return self.nombre


class TipoDano(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=500, verbose_name='Descripción')
    valor = models.IntegerField(verbose_name='Valor')
    mano_obra = models.IntegerField(verbose_name='Mano de obra')

    # class Meta:
    #     managed = False
    #     db_table = 'tipo_dano'
    #     verbose_name_plural = 'Tipo Daños'

    def __str__(self):
        return self.nombre


class TipoPlan(models.Model):
    nombre = models.CharField(max_length=60, verbose_name='Nombre')
    descripcion = models.CharField(max_length=500, verbose_name='Descripción')
    valor = models.IntegerField(verbose_name='Valor')
    cobertura_max = models.IntegerField(verbose_name='Cobertura Máxima')
    deducible = models.IntegerField(verbose_name='Deducible')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'tipo_plan'
    #     verbose_name_plural = 'Tipo Planes'

    def __str__(self):
        return self.nombre


class TipoVehiculo(models.Model):
    tipo = models.CharField(max_length=20, verbose_name='Tipo')

    # class Meta:
    #     managed = False
    #     db_table = 'tipo_vehiculo'
    #     verbose_name_plural = 'Tipo Vehículo'

    def __str__(self):
        return self.tipo


class UsuarioManager(BaseUserManager):
    def create_user(self, email, rut_usuario, primer_nombre, primer_apellido, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo')

        usuario = self.model(
            rut_usuario=rut_usuario,
            email=self.normalize_email(email),
            primer_nombre=primer_nombre,
            primer_apellido=primer_apellido
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email, rut_usuario, primer_nombre, primer_apellido, password):
        usuario = self.create_user(
            email,
            rut_usuario=rut_usuario,
            primer_nombre=primer_nombre,
            primer_apellido=primer_apellido,
            password=password
        )
        usuario.is_administrador = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):

    opciones = [
        ("1", 'Mesa de Ayuda'),
        ("2", 'Liquidador'),
        ("3", 'Personal Taller'),
        ("4", 'Personal Grua'),
    ]

    rut_usuario = models.CharField(
        unique=True, max_length=10, verbose_name='Rut Usuario')
    primer_nombre = models.CharField(
        max_length=20, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(
        max_length=20, verbose_name='Segundo Nombre', null=True)
    primer_apellido = models.CharField(
        max_length=20, verbose_name='Apellido Paterno')
    segundo_apellido = models.CharField(
        max_length=20, verbose_name='Apellido Materno', null=True)
    email = models.EmailField(
        max_length=254, verbose_name='Correo', unique=True)
    telefono = models.CharField(
        verbose_name='Teléfono', null=True, max_length=9)
    rol = models.CharField(max_length=30, choices=opciones, null=True)
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller', blank=True, null=True)
    servicio_grua_id_servicio_grua = models.ForeignKey(
        'ServicioGrua', models.DO_NOTHING, db_column='servicio_grua_id_servicio_grua', verbose_name='Servicio Grua', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_administrador = models.BooleanField(default=False)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    objects = UsuarioManager()

    USERNAME_FIELD = 'rut_usuario'
    REQUIRED_FIELDS = ['email', 'primer_nombre', 'primer_apellido']

    # class Meta:
    #     managed = False
    #     db_table = 'usuario'
    #     verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.rut_usuario

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_administrador


class Vehiculo(models.Model):
    patente_vehiculo = models.CharField(
        primary_key=True, max_length=8, verbose_name='Patente')
    anio = models.CharField(verbose_name='Año', max_length=4)
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    nro_motor = models.CharField(max_length=100, verbose_name='N° Motor')
    tipo_vehiculo_id_tipo_auto = models.ForeignKey(
        'TipoVehiculo', models.DO_NOTHING, db_column='tipo_vehiculo_id_tipo_auto', verbose_name='Tipo Vehículo', null=True)
    marca_id_marca = models.ForeignKey(
        'Marca', models.DO_NOTHING, db_column='marca_id_marca', verbose_name='ID Marca', null=True)
    asegurado_rut_asegurado = models.ForeignKey(
        'Asegurado', models.DO_NOTHING, db_column='asegurado_rut_asegurado', verbose_name='Rut Asegurado', null=True)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    # class Meta:
    #     managed = False
    #     db_table = 'vehiculo'
    #     verbose_name_plural = 'Vehículos'

    def __str__(self):
        return self.patente_vehiculo

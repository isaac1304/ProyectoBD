from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Curso(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=56)
    creditos = models.PositiveBigIntegerField()
    
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'
        
class Cliente(models.Model):
    cedula_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido_1 = models.CharField(max_length=50, blank=True, null=True)
    apellido_2 = models.CharField(max_length=50, blank=True, null=True)
    nacimiento = models.DateField(blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'

class Colaboradores(models.Model):
    id_colaborador = models.AutoField(primary_key=True)
    cedula_colaborador = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido_1 = models.CharField(max_length=50, blank=True, null=True)
    apellido_2 = models.CharField(max_length=50, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    puesto = models.CharField(max_length=50, blank=True, null=True)
    col_direccion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colaboradores'

class Devoluciones(models.Model):
    id_devolucion = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    dev_ced_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='dev_ced_cliente', blank=True, null=True)
    dev_cod_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='dev_cod_producto', blank=True, null=True)
    dev_cod_factura = models.ForeignKey('Facturas', models.DO_NOTHING, db_column='dev_cod_factura', blank=True, null=True)
    monto_devolucion = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devoluciones'

class Facturas(models.Model):
    cod_factura = models.AutoField(primary_key=True)
    fac_ced_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='fac_ced_cliente', blank=True, null=True)
    fac_cod_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='fac_cod_producto', blank=True, null=True)
    fac_id_colaborador = models.ForeignKey(Colaboradores, models.DO_NOTHING, db_column='fac_id_colaborador', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facturas'

class Productos(models.Model):
    cod_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    pro_id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='pro_id_categoria', blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'

class Proveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores'

class Sucursales(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursales'

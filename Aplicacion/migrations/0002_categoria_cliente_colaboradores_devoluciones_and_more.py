# Generated by Django 4.1.7 on 2023-03-28 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'categoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cedula_cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_1', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_2', models.CharField(blank=True, max_length=50, null=True)),
                ('nacimiento', models.DateField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Colaboradores',
            fields=[
                ('id_colaborador', models.AutoField(primary_key=True, serialize=False)),
                ('cedula_colaborador', models.CharField(blank=True, max_length=10, null=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_1', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_2', models.CharField(blank=True, max_length=50, null=True)),
                ('correo', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('puesto', models.CharField(blank=True, max_length=50, null=True)),
                ('col_direccion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'colaboradores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Devoluciones',
            fields=[
                ('id_devolucion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('monto_devolucion', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'devoluciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('cod_factura', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('total_pagado', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'facturas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('cod_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'productos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('correo', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'proveedores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id_sucursal', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'sucursales',
                'managed': False,
            },
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-28 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0002_categoria_cliente_colaboradores_devoluciones_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.IntegerField(max_length=6, primary_key=True, serialize=False),
        ),
    ]

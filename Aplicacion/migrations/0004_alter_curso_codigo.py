# Generated by Django 4.1.7 on 2023-03-28 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0003_alter_curso_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

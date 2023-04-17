# ProyectoBD
Proyecto Base de Datos Camil Briceño, Sebastian Campos, Isaac Granados y Antony Fajardo.

Universidad Fidélitas 
 
 
 
SC-504: Lenguaje de Bases de Datos. 
 
Prof.: Randall Alonso Leitón Jiménez 

Primer Cuatrimestre, año 2023 

Instrucciones para correr el proyecto:

1. Instalar Python 3.10.10

 

*********CMD*********
Validadar version de Python y la de PIP
python --version
pip --version

 

2. Instalar paquete Django
pip install Django==4.1.7

 

3. Installar paquete para usar oracle en Django
pip install cx_oracle

 

4. Instalar paquete del entorno virtual para poder compilar el proyecto
pip install virtualenv

 

5. Crear el proyecto en el escritorio
django-admin startproject Proyecto .

 

********Visual Studio Code*********
Ejecutar proyecto y validar que compila
python manage.py runserver

 

*********Settings*********
Conexion de la base de datos de oracle con el proyecto
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'orcl',
        'USER': 'PROYECTO',
        'PASSWORD': 'P4$$woRD',
        'HOST': '',
        'PORT': '',
    }
}

 

Ejecutar migracion inicial
python manage.py migrate

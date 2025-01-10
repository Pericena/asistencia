# asistencia
Sistema de asistencia con django 
python -m venv venv
venv\Scripts\activate
pip install django psycopg2
django-admin --version
django-admin startproject conexion_bd
cd 
python manage.py startapp db_conexion

cd conexion_bd
python manage.py startapp db_conexion

1. Instalación de dependencias
Asegúrate de tener Python y PostgreSQL instalados en tu sistema. Luego, instala Django y psycopg2, que es el adaptador para PostgreSQL:

pip install django psycopg2
1. Crear el proyecto Django
Ejecuta el siguiente comando para crear un nuevo proyecto Django:

django-admin startproject conexion_bd
1. Configurar PostgreSQL en el proyecto

CREATE DATABASE mi_base_datos;
Abre el archivo settings.py de tu proyecto y configura la base de datos para que utilice PostgreSQL. Dentro de DATABASES, cambia la configuración para que se vea así:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mi_base_datos',  # El nombre de tu base de datos
        'USER': 'tu_usuario',     # El usuario de PostgreSQL
        'PASSWORD': 'tu_contraseña',  # La contraseña del usuario
        'HOST': 'localhost',      # Si estás usando PostgreSQL en local
        'PORT': '5432',           # Puerto por defecto de PostgreSQL
    }
}

1. Crear una aplicación dentro del proyecto
Dentro del directorio del proyecto (conexion_bd), crea una nueva aplicación para manejar las vistas:

cd conexion_bd

python manage.py startapp db_conexion

1. Crear una vista para mostrar el mensaje
En el archivo views.py de la aplicación db_conexion, crea una vista que imprima "Conexión de base de datos":

from django.shortcuts import HttpResponse
from django.db import connections

def conexion_base_datos(request):
    try:
        # Probar la conexión
        with connections['default'].cursor() as cursor:
            cursor.execute("SELECT 1")
        return HttpResponse("Conexión de base de datos exitosa")
    except Exception as e:
        return HttpResponse(f"Error de conexión: {str(e)}")

1. Configurar las URLs
En el archivo urls.py de tu proyecto (conexion_bd/urls.py), incluye la nueva vista:

from django.contrib import admin
from django.urls import path
from db_conexion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conexion/', views.conexion_base_datos),  # Ruta para la vista
]
1. Agregar la aplicación a INSTALLED_APPS
En el archivo settings.py, agrega tu aplicación db_conexion en la lista de INSTALLED_APPS:


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'db_conexion',  # Agregar aquí
]



Migrar la base de datos
Ejecuta las migraciones para que Django cree las tablas necesarias en PostgreSQL:python manage.py migrate

Inicia el servidor de desarrollo de Django:

python manage.py runserver

Abre un navegador web y navega a:

arduino
Copiar código
http://127.0.0.1:8000/conexion/
Si la configuración es correcta y PostgreSQL está funcionando, deberías ver el mensaje "Conexión de base de datos exitosa".


from django.shortcuts import render
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
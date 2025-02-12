from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from inicio.models import Usuario

# Create your views here.

def obtener_usuario():
    global usuario_ingresado
    archivo = open("usuario.txt", "r")
    usuario_ingresado = Usuario.objects.get(nombre_de_usuario=archivo.readLine())
    archivo.close()

def mostrar_perfil(request):
    obtener_usuario()
    nombre_completo = usuario_ingresado.nombre + " " + usuario_ingresado.apellido

    return render(request, "perfil.html",{
        "nombre_usuario": usuario_ingresado.nombre_de_usuario,
        "puntuacion": usuario_ingresado.puntuacion_c_mas_mas+usuario_ingresado.puntuacion_python+usuario_ingresado.puntuacion_go,
        "puntos_c":usuario_ingresado.puntuacion_c_mas_mas,
        "puntos_py":usuario_ingresado.puntuacion_python,
        "puntos_go":usuario_ingresado.puntuacion_go,
        "nombre": nombre_completo if nombre_completo else "--",
        "link": usuario_ingresado.url if usuario_ingresado.url else "--",
        "text": usuario_ingresado.sobre_mi if usuario_ingresado.sobre_mi else "--",
        })

def agregar_info(request):
    pass
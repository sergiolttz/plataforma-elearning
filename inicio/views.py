from django.shortcuts import render

from django.shortcuts import HttpResponse, HttpResponseRedirect
from .models import Usuario

# Create your views here.

def pagina_inicio(request):
    return render(request, "inicio.html")

def registro_login(request):
    entrada = request.POST.get('entrada').split()

    if len(entrada)==4:
        cont=0

        for i in entrada:
            if entrada.count(i) == 2 and len(i)>7:
                contraseña = i; cont +=1
                print("la contraseña es: ", {contraseña})
            
            if ("@" in i) and (entrada.count(i)==1):
                correo = i; cont +=1
            
            if not "@" in i and (entrada.count(i)==1):
                nombre_de_usuario = i; cont +=1

        if cont == 4:
            usuario_nuevo = Usuario()
            usuario_nuevo.nombre_de_usuario = nombre_de_usuario
            usuario_nuevo.correo = correo
            usuario_nuevo.contraseña = contraseña
            usuario_nuevo.save()
            return render(request, "inicio.html")

    elif len(entrada)==2:
        try:
            print(entrada[0])
            usuario_ingresado = Usuario.objects.get(nombre_de_usuario=entrada[0])
        except:
            try:
                print (entrada[1])
                usuario_ingresado = Usuario.objects.get(nombre_de_usuario=entrada[1])
            except:
                print("ERROR")
                return HttpResponse("No ha respetado el formato indicaro, vuelva a intentarlo")
        
        if usuario_ingresado.contraseña == entrada[0] or usuario_ingresado.contraseña==entrada[1]:
            archivo = open("usuario.txt","w")
            archivo.write(str(usuario_ingresado.nombre_de_usuario))
            archivo.close()
            return HttpResponseRedirect("/perfil/mostrar_perfil/")
        
    return HttpResponse("No ha respetado el formato indicado, vuelva a intentarlo")          

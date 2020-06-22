from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import User, Archivo, Carpeta
from .models import Task, Category
from datetime import *
import os

#El Index lo documente por ahora para el todolist, pero de ahi lo cambiamos, no lo quiero borrar porque a futuro
#   puede ser util tenerlo.

#Shows the index of the project. It shows different information depending if the
#   user is authenticated or not.
#   The user can enter information and then send a POST request to add a task to the list
#   This method has the main functionality of the project
def index(request): #the index view
    #folders = Carpeta.objects.all()
    #todos = Task.objects.filter(owner=request.user)
    if request.method == 'GET':
        return render(request, "drive/index.html")
    if request.method == "POST": #checking if the request method is a POST
        
        if 'login' in request.POST: #Log In
            mail = request.POST['mail']
            contraseña = request.POST['contraseña']
            print('mail:' +mail+'pass: '+contraseña) ## No loguea :c
            usuario = authenticate(request,username=mail,password=contraseña)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, 'Te damos la bienvenida ' + usuario.apodo + '!')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'No hubo match para los datos ingresados.')
                return HttpResponseRedirect('/')
        else: #Register
            nombre = request.POST['Nombre']
            apellido =  request.POST['Apellido']
            contraseña = request.POST['contraseña']
            apodo = request.POST['apodo']
            mail = request.POST['mail']
            if not User.objects.filter(username=mail).exists():
                user = User.objects.create_user(username=mail, password=contraseña,email=mail,apodo=apodo, 
                first_name= nombre, last_name=apellido)
                carpeta_raiz = Carpeta(nombre = 'Raiz', usuario = user)
                carpeta_raiz.save()
                messages.success(request, 'Se creó el usuario para ' + user.apodo + '! (carpeta '+carpeta_raiz.nombre+' creada)')
            else:
                messages.error(request, 'Ya existe un usuario con ese email. Intenta iniciando sesión con tu email y contraseña.')
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('/')
        
#Called with /logout, only available if the user is authenticated
#   Logouts the authenticated user and shows the screen as if is not registered
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

#Called with /profile, only available por aunthenticated users and shows
#   the user information displayed in the screen
@login_required
def view_profile(request):
    
    if request.method == 'GET':
        return render(request, "drive/profile.html")
    
    if request.method == "POST": #checking if the request method is a POST
        usuario = request.user

        usuario = request.user
        
        if 'profilepic' in request.POST: #Log In
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
            if request.FILES['adjunto']:
                old = usuario.avatar
                usuario.avatar  = request.FILES['adjunto']
                usuario.avatar.name = usuario.first_name + "##" + usuario.last_name + "##" + str(datetime.now()) +".png"
                if old != None:
                    os.remove(os.path.join(MEDIA_ROOT, old.name))

        else:
            usuario.first_name       = request.POST['Nombre']
            usuario.last_name        = request.POST['Apellido']
            usuario.apodo            = request.POST['Apodo']
            usuario.descripcion      = request.POST['Descripcion']
            if request.POST['Nacimiento']:
                usuario.fecha_nacimiento = request.POST['Nacimiento']

        # Modifica valores
        usuario.save()
        messages.success(request, 'Se modificaron tus datos!')
        return HttpResponseRedirect('/profile')


    #Dejo aqui abierto por si queremos hacer un post que cambie los atributos
    pass
@login_required
def view_files(request):
    files = Archivo.objects.all()
    if request.method == 'GET':
        return render(request, "drive/datafiles.html",{"files": files})
    #Dejo aqui abierto por si queremos hacer un post que cambie los atributos
    pass
#Called with /profile, only available por aunthenticated users and shows
#   the user information displayed in the screen
@login_required
def upload_file(request):
    
    #if request.user.is_authenticated:
    # archivos = Archivo.objects.filter(usuario=request.user)

    if request.method == 'GET':
        return render(request, "drive/profile.html")
    
    if request.method == "POST": #checking if the request method is a POST

        if request.FILES['Archivo']:
            Carpetas = Carpeta.objects.filter(usuario = request.user)
            archivo_nuevo = request.FILES['Archivo'] # archivo
            carpeta = request.POST['Carpeta']  # seleccionar carpeta
            nombre = archivo_nuevo.name
            formato = archivo_nuevo.name.split(".")[1]
            usuario = request.user
            archive = Archivo(nombre = nombre, formato = formato, usuario = usuario, carpeta = carpeta)
            archive.save()
            # Modifica valores
            return HttpResponseRedirect('/')
            messages.success(request, 'Archivo subido!')
        # editar avatar
    pass
    #Dejo aqui abierto por si queremos hacer un post que cambie los atributos
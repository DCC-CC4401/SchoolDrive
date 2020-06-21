from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from drive.models import User, Archivo
from .models import Task, Category


#El Index lo documente por ahora para el todolist, pero de ahi lo cambiamos, no lo quiero borrar porque a futuro
#   puede ser util tenerlo.

#Shows the index of the project. It shows different information depending if the
#   user is authenticated or not.
#   The user can enter information and then send a POST request to add a task to the list
#   This method has the main functionality of the project
def index(request): #the index view

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
                messages.success(request, 'Se creó el usuario para ' + user.apodo + '!')
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

        if 'profilepic' in request.POST: #Log In
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
            if request.FILES['adjunto']:
                old = usuario.profile_picture
                usuario.profile_picture  = request.FILES['adjunto']
                usuario.profile_picture.name = usuario.first_name + "##" + usuario.last_name + "##" + str(datetime.now()) +".png"
                os.remove(os.path.join(MEDIA_ROOT, old.name))

        else:

        usuario = request.user
        usuario.first_name       = request.POST['Nombre']
        usuario.last_name        = request.POST['Apellido']
        usuario.apodo            = request.POST['Apodo']
        usuario.descripcion      = request.POST['Descripcion']
        usuario.fecha_nacimiento = request.POST['Nacimiento']

        

        # editar avatar
        if request.FILES['Avatar']:
            avatar = request.FILES['Avatar']
            usuario.avatar = avatar
        usuario.save()
        # Modifica valores
        messages.success(request, 'Se modificaron tus datos!')
        return HttpResponseRedirect('/')


    #Dejo aqui abierto por si queremos hacer un post que cambie los atributos
    pass

#Called with /files, only available for aunthenticated users and shows
#   the user information displayed in the screen
@login_required
def view_files(request):
    
    if request.method == 'GET':
        return render(request, "drive/datafiles.html")

    #Dejo aqui abierto por si queremos hacer un post que cambie los atributos
    pass

#Called with /profile, only available por aunthenticated users and shows
#   the user information displayed in the screen
@login_required
def upload_file(request):
    
    #if request.user.is_authenticated:
    #    archivos = Archivo.objects.filter(usuario=request.user)

    if request.method == 'GET':
        return render(request, "drive/profile.html")
    
    if request.method == "POST": #checking if the request method is a POST

        

        if request.FILES['Archivo']:
            archive = Archivo()
            archivo_nuevo = request.FILES['Archivo']
            archive.archivo = archivo_nuevo
            archive.nombre = archivo_nuevo.name.split(".")[0]
            archive.formato = archivo_nuevo.name.split(".")[1]
            archive.usuario = request.user
            archive.save()
            # Modifica valores
            messages.success(request, 'Archivo subido!')
            return HttpResponseRedirect('/')
        
        # editar avatar
        
        
        


    #Dejo aqui abierto por si queremos hacer un post que cambie los atributos
    pass
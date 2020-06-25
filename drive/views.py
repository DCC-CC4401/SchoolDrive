from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.utils.encoding import *
from .models import User, Archivo, Carpeta
from datetime import *
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AVATAR_ROOT = os.path.join(BASE_DIR, 'media/avatars')
FILES_ROOT  = os.path.join(BASE_DIR, 'media/archivos')
# El Index lo documente por ahora para el todolist, pero de ahi lo cambiamos, no lo quiero borrar porque a futuro
# puede ser util tenerlo.

# Shows the index of the project. It shows different information depending if the
# user is authenticated or not.
# The user can enter information and then send a POST request to add a task to the list
def index(request): # the index view
    
    if request.method == 'GET':
        return render(request, "drive/index.html")
    if request.method == "POST": #checking if the request method is a POST
        
        if 'login' in request.POST: #Log In
            mail = request.POST['mail']
            contraseña = request.POST['contraseña']
            #print('mail:' +mail+'pass: '+contraseña)
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
                user = User.objects.create_user(username=mail, password=contraseña,email=mail,apodo=apodo, first_name= nombre, last_name=apellido)
                new_carpeta_raiz = Carpeta(nombre = 'Raiz', usuario = user)
                user.carpeta_raiz = new_carpeta_raiz.id
                user.save()
                new_carpeta_raiz.save()
                messages.success(request, 'Se creó el usuario para ' + user.apodo + '! (carpeta '+new_carpeta_raiz.nombre+' creada)')
            else:
                messages.error(request, 'Ya existe un usuario con ese email. Intenta iniciando sesión con tu email y contraseña.')
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('/')
        
# Called with /logout, only available if the user is authenticated
# Logouts the authenticated user and shows the screen as if is not registered
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

# Called with /profile, only available por aunthenticated users and shows
# the user information displayed in the screen
@login_required
def view_profile(request):
    
    if request.method == 'GET':
        return render(request, "drive/profile.html")
    
    if request.method == "POST": #checking if the request method is a POST
        usuario = request.user

        if 'profilepic' in request.POST: #Edit Picture
            
            if request.FILES['adjunto']:
                old = usuario.avatar
                usuario.avatar  = request.FILES['adjunto']
                usuario.avatar.name = usuario.first_name + "##" + usuario.last_name + "##" + str(datetime.now()) +".png"
                if old != None:
                    os.remove(os.path.join(AVATAR_ROOT, old.name))

        else: # Edit Info
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

def functiontest():
    return "Hola"

def tree_Folders(carpeta):
    hijos = Carpeta.objects.filter(padre = carpeta)
    html = ""
    for hijo in hijos:
        if (Carpeta.objects.filter(padre = hijo).count()>0):
            html = html + '<li data-icon-cls="fa fa-folder"><a href='+str(hijo.id)+'>'+hijo.nombre+'</a><ul>'+tree_Folders(hijo)+'</ul></li>'
        else:
            html = html + '<li data-icon-cls="fa fa-folder"><a href='+str(hijo.id)+'>'+hijo.nombre+'</a></li>'
    return html

# Called with /files, only available por aunthenticated users and shows
# the user files and folders
@login_required
def view_files(request, folderid):

    current_folder = Carpeta.objects.filter(id=folderid,usuario=request.user)[0]
    tree_folder = tree_Folders(Carpeta.objects.filter(id=request.user.carpeta_raiz,usuario=request.user)[0])
    html_carpetaraiz = '<li data-icon-cls="fa fa-folder active"><a href='+request.user.carpeta_raiz+'>'+"Root"+'</a><ul>'+tree_folder+'</ul></li>'
    files = Archivo.objects.filter(usuario=request.user, carpeta=current_folder)
    folders = Carpeta.objects.filter(usuario=request.user)
    formatos_img = ['jpg','png','jepg','gif']
    formatos_vid = ['mp4','avi','mepg']
    formatos_msc = ['mp3','wma']
    formatos_doc = ['txt','doc','docx','ots']
    formatos_xcl = ['xlsx','xls','csv','tsv']

    diccionario = {"files": files, "folders":folders, "formatos_img":formatos_img, 
    "formatos_vid": formatos_vid, "formatos_msc":formatos_msc, "tree_folder":html_carpetaraiz, "current_folder":current_folder}

    if request.method == 'GET':
        return render(request, "drive/datafiles.html", diccionario)

    if request.method == "POST": #checking if the request method is a POST
        if 'Upload_file' in request.POST and  request.FILES['archivo']:
            archivo = request.FILES['archivo'] # archivo
            carpeta_name = request.POST['folder']  # seleccionar carpeta
            nombre  = request.POST['nombre']
            formato = archivo.name.split(".")[1]
            usuario = request.user

            carpeta = Carpeta.objects.get(usuario = usuario, nombre= carpeta_name)
           
            archivo.name = nombre + "." + formato
            
            archive = Archivo(archivo=archivo, nombre = nombre, formato = formato, usuario = usuario, carpeta = carpeta)
            archive.save()
            # Modifica valores
            return HttpResponseRedirect('/files/'+str(current_folder.id))
            messages.success(request, 'Archivo subido!')
        
        elif 'deleteFiles' in request.POST:
            toDelete = []
            for element in request.POST:
                toDelete.append(element)
            toDelete = toDelete[7:] #Primeros 4 elementos no importan en este form
            filesToDelete = []
            for fileRoute in toDelete:
                #print("aborrars " + fileRoute)
                if "/" in fileRoute:
                    borrarArchivo(fileRoute, request)
                else:
                    borrarCarpeta(fileRoute,request)

            messages.success(request, 'Archivos borrados!')
            return HttpResponseRedirect('/files/'+str(current_folder.id))

        elif "new_folder" in request.POST:
            usuario = request.user
            nombre_carpeta = request.POST['newFolder']
            #carpeta_padre = Carpeta.objects.filter(usuario=request.user) #Descomentar si no funciona bien la carpeta_padre de abajo, son experimentos.
            carpeta_padre = Carpeta.objects.filter(usuario=request.user, nombre=request.POST['newOriginFolder'] )[0]
            carpeta = Carpeta(nombre = nombre_carpeta, usuario = usuario, padre = carpeta_padre)
            carpeta.save()
            messages.success(request, 'Carpeta creada!')
            return HttpResponseRedirect('/files/'+str(current_folder.id))

        # editar avatar
    #Dejo aqui abierto por si queremos hacer un post que cambie los atributos
    pass


def borrarArchivo(fileRoute, request):
    print("Por borrar: "+fileRoute)
    folder = fileRoute.split("/")[0]
    rest   = fileRoute.split("/")[1]
    f_name = rest.split(".")[0]
    formato= rest.split(".")[1]
    archivo = Archivo.objects.get(nombre=f_name,formato=formato,usuario=request.user,carpeta=folder)
    archivo.delete()
    os.remove(os.path.join(FILES_ROOT, f_name+"."+formato))
    print(archivo.nombre+" borrado satisfactoriamente :)")

def borrarCarpeta(fileRoute,request):
    carpeta = Carpeta.objects.get(id=fileRoute, usuario=request.user)
    archivosEnCarpeta = Archivo.objects.filter(usuario=request.user, carpeta=fileRoute)
    for archivo in archivosEnCarpeta:
        print("Borrando "+archivo.nombre+"."+archivo.formato)
        archivo.delete()
        os.remove(os.path.join(FILES_ROOT, archivo.nombre+"."+archivo.formato))
    carpetasEnCarpeta = Carpeta.objects.filter(padre=carpeta)
    for folder in carpetasEnCarpeta:
        borrarCarpeta(folder.id,request)
    carpeta.delete()


#Called inside /files, it is used to upload a file after selecting one from storage
#   The file is uploaded
@login_required
def upload_file(request):
    
    #if request.user.is_authenticated:
    # archivos = Archivo.objects.filter(usuario=request.user)

    if request.method == 'GET':
        return render(request, "drive/profile.html")
    
    if request.method == "POST": #checking if the request method is a POST

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
    pass
    #Dejo aqui abierto por si queremos hacer un post que cambie los atributos

#Called inside /files, it is used to create a subfolder in the selected directory,
#@login_required
#def create_folder(request):
#
#    if request.method == 'GET':
#        return render(request, "drive/datafiles.html")
#
#    if request.method == 'POST':
#       usuario = request.user
 #       nombre_carpeta = request.POST['NombreCarpeta']
#        carpeta_padre = Carpeta.objects.filter(usuario=request.user) #Descomentar si no funciona bien la carpeta_padre de abajo, son experimentos.
#        carpeta_padre = request.POST['Carpeta'] #Esto si la hacemos con carpeta actual
 #       carpeta = Carpeta(nombre = nombre_carpeta, usuario = usuario, padre = carpeta_padre)
#        carpeta.save()
#       return HttpResponseRedirect('/')
 #       messages.success(request, 'Carpeta creada!')
#
 #   pass
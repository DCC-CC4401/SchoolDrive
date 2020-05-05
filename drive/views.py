from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from drive.models import User
from .models import Task, Category

#El Index lo documente por ahora para el todolist, pero de ahi lo cambiamos, no lo quiero borrar porque a futuro
#   puede ser util tenerlo.

#Shows the index of the project. It shows different information depending if the
#   user is authenticated or not.
#   The user can enter information and then send a POST request to add a task to the list
#   This method has the main functionality of the project
def index(request): #the index view
    # if request.user.is_authenticated:
    #     todos = Task.objects.filter(owner=request.user) #quering all todos with the object manager
    # else:
    #     todos= Task.objects.filter(owner=None)
    # categories = Category.objects.all() #getting all categories with object manager
    # if request.method=="GET":
    #     return render(request, "drive/index.html", {"todos": todos, "categories": categories})
    if request.method == 'GET':
        return render(request, "drive/index.html")
    if request.method == "POST": #checking if the request method is a POST
        
        if 'login' in request.POST: #Log In
            mail = request.POST['mail']
            contraseña = request.POST['contraseña']
            usuario = authenticate(request,email=mail,password=contraseña)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, 'Te damos la bienvenida ' + usuario.apodo + '!')
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/register')
        else: #Register
            nombre = request.POST['nombre']
            contraseña = request.POST['contraseña']
            apodo = request.POST['apodo']
            mail = request.POST['mail']
            user = User.objects.create_user(username=nombre, password=contraseña,email=mail,apodo=apodo)
            messages.success(request, 'Se creó el usuario para ' + user.apodo + '!')
            return HttpResponseRedirect('/')

        # if "taskAdd" in request.POST: #checking if there is a request to add a todo
        #     title = request.POST["description"] #title
        #     date = str(request.POST["date"]) #date
        #     category = request.POST["category_select"] #category
        #     content = title + " -- " + date + " " + category #content
        #     if request.user.is_authenticated:
        #         Todo = Task(title=title, content=content, due_date=date, category=Category.objects.get(name=category),owner=request.user)
        #     else:
        #         Todo = Task(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
        #     Todo.save() #saving the todo
        #     return redirect("/") #reloading the page
        # if "taskDelete" in request.POST: #checking if there is a request to delete a todo
        #     checkedlist = request.POST["checkedbox"] #checked todos to be deleted
        #     for todo_id in checkedlist:
        #         print(todo_id,"Todo id")
        #         todo = Task.objects.get(id=int(todo_id)) #getting todo id
        #         todo.delete() #deleting todo
        #     return render(request, "drive/index.html", {"todos": todos, "categories": categories})

#Called with /register, it is available if the user is not authenticated, and renders
#   the view where the user can enter the necessary to have an account.
#   The user can call the url by GET, or can add information and then POST to create an account
def register_user(request):
    if request.method == 'GET':
        return render(request,"drive/register_user.html")

    elif request.method == 'POST':
        nombre = request.POST['nombre']
        contraseña = request.POST['contraseña']
        apodo = request.POST['apodo']
        mail = request.POST['mail']
        user = User.objects.create_user(username=nombre, password=contraseña,email=mail,apodo=apodo)
        messages.success(request, 'Se creó el usuario para ' + user.apodo + '!')
        return HttpResponseRedirect('/')

#Called with /login, only available if the user is not authenticated
#   Logins the user and begins to display the interface for aunthenticated users (if the user ir registered)
#   Has two options depending if the user is giving information or just getting it
def login_user(request):
    if request.method == 'GET':
        return render(request, "drive/login.html")
    if request.method == 'POST':
        
            username = request.POST['username']
            contraseña = request.POST['contraseña']
            usuario = authenticate(request,username=username,password=contraseña)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, 'Te damos la bienvenida ' + usuario.apodo + '!')
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/register')
        
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
        nombreDeUsuario = request.user.username
        nombre = request.user.first_name
        apellido = request.user.last_name
        mail = request.user.email
        apodo = request.user.apodo
        return render(request, "drive/profile.html")

    #Dejo aqui abierto por si queremos hacer un post que cambie los atributos
    pass
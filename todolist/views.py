from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect

from .models import Task, Category
def index(request): #the index view
    if request.user.is_authenticated:
        todos = Task.objects.filter(owner=request.user) #quering all todos with the object manager
    else:
        todos= Task.objects.filter(owner=None)
    categories = Category.objects.all() #getting all categories with object manager
    if request.method=="GET":
        return render(request, "todolist/index.html", {"todos": todos, "categories": categories})
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            if request.user.is_authenticated:
                Todo = Task(title=title, content=content, due_date=date, category=Category.objects.get(name=category),owner=request.user)
            else:
                Todo = Task(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo
            return redirect("/") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                print(todo_id,"Todo id")
                todo = Task.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo
            return render(request, "todolist/index.html", {"todos": todos, "categories": categories})


from todolist.models import User
def register_user(request):
    if request.method == 'GET':
        return render(request,"todolist/register_user.html")

    elif request.method == 'POST':
        nombre = request.POST['nombre']
        contraseña = request.POST['contraseña']
        apodo = request.POST['apodo']
        mail = request.POST['mail']
        user = User.objects.create_user(username=nombre, password=contraseña,email=mail,apodo=apodo)
        messages.success(request, 'Se creó el usuario para ' + user.apodo + '!')
        return HttpResponseRedirect('/')


def login_user(request):
    if request.method == 'GET':
        return render(request,"todolist/login.html")
    if request.method == 'POST':
        username = request.POST['username']
        contraseña = request.POST['contraseña']
        usuario = authenticate(request,username=username,password=contraseña)
        if usuario is not None:
            login(request,usuario)
            messages.success(request, 'Te damos la bienvenida ' + usuario.apodo + '!')
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/register')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
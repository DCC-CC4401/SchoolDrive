from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    apodo = models.CharField(max_length=30)
    descripcion = models.TextField(blank = True)
    fecha_cumpleanhos = models.DateField(null = True)
    class Meta:
        unique_together = ['email']
    
class Archivo(models.Model):
    class Meta:
        unique_together = ['nombre', 'formato', 'usuario_correo']
    nombre = models.CharField(max_length = 250)
    formato = models.CharField(max_length = 250)
    usuario_correo = models.ForeignKey(User, db_column="email", on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name #name to be shown when called



class Task(models.Model): #drive able name that inherits models.Model
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    category = models.ForeignKey(Category, default="general", on_delete=models.SET_DEFAULT) # a foreignkey
    owner = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"] #ordering by the created field

    def __str__(self):
        return self.title #name to be shown when called
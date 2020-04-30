from django.contrib import admin

# Register your models here.
from todolist import models

admin.site.register(models.Category)
admin.site.register(models.Task)
admin.site.register(models.User)
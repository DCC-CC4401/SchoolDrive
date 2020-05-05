from django.contrib import admin

# Register your models here.
from drive import models

admin.site.register(models.Category)
admin.site.register(models.Task)
admin.site.register(models.User)
admin.site.register(models.Archivo)
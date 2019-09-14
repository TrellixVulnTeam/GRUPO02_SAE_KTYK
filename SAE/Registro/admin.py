from django.contrib import admin
from .models import *

# Register your models here.
from django.contrib.auth.models import Permission
from django.contrib import admin
admin.site.register(Permission)
admin.site.register(Profesor)
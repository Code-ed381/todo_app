from django.contrib import admin
from .models import Todo,Completed

# Register your models here.
admin.site.register(Todo)
admin.site.register(Completed)
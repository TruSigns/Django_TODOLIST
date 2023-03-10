from django.contrib import admin
from .models import Task
# Register your models here.

# Adding the table to the admin page

admin.site.register(Task)
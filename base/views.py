from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task


# Create your views here.

class TaskList(ListView):
    model = Task
    # Giving it a name to make it easy to use in code blocks
    context_object_name = 'tasks'

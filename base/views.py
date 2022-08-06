from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task


class TaskList(ListView):
    # it will be rendered to html
    model = Task
    # represent query list i.e. tasks it will go to task_list.html as object_list
    context_object_name = 'tasks'

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task


class TaskList(ListView):
    # it will be rendered to html
    model = Task
    # represent query list i.e. tasks it will go
    # to task_list.html as object_list
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    # it will be rendered to html
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'  # previously task_detail.html
    # normally task_detail.hmtl name is made as Task from model name and detail from this class name

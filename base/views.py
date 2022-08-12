from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task


class TaskList(ListView):
    # it will be rendered to html
    model = Task  # the db classes we have made in models.py and those were migrated
    # represent query list i.e. tasks it will go
    # to task_list.html as object_list
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    # it will be rendered to html
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'  # previously task_detail.html
    # normally task_detail.hmtl name is made as Task from model name and detail from this class name


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'  # e.g. ['title','description']
    success_url = reverse_lazy('tasks')  # 'tasks is url name'


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'  # e.g. ['title','description']
    success_url = reverse_lazy('tasks')  # 'tasks is url name'


class TaskDelete(DeleteView):
    model = Task
    fields = '__all__'  # e.g. ['title','description']
    success_url = reverse_lazy('tasks')  # 'tasks is url name'
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')  # 'tasks is url name'

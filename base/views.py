from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

# 'tasks' is main page


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    # if user is currently logged in this will send to destination page
    redirect_authenticated_user = True

    def get_success_url(self):
        # this method triggered automatically on post request
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin, ListView):
    # it will be rendered to html
    model = Task  # the db classes we have made in models.py and those were migrated
    # represent query list i.e. tasks it will go
    # to task_list.html as object_list
    context_object_name = 'tasks'

    # user can't see other users data , can see only his
    # it is automatically triggered
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    # it will be rendered to html
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'  # previously task_detail.html
    # normally task_detail.hmtl name is made as Task from model name and detail from this class name


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # fields = '__all__'  # e.g. ['title','description']
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')  # 'tasks is url name'

    def form_valid(self, form):
        # it is automatically triggered on post request
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    # fields = '__all__'  # e.g. ['title','description']
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')  # 'tasks is url name'


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    fields = '__all__'  # e.g. ['title','description']
    success_url = reverse_lazy('tasks')  # 'tasks is url name'
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')  # 'tasks is url name'

from django.shortcuts import render
from .models import Task
# Create your views here.

def index(request):
    task = Task.objects.all()
    return render(request, 'tasks/task_list.html', {
        'task': task
    })
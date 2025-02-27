from django.shortcuts import render
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
    task = Task.objects.all()
    return render(request, 'tasks/task_list.html', {
        'task': task
    })

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = TaskForm()

    return render(request, 'tasks/create_task.html', {
        'form': form
    })
from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

def index(request):
    task = Task.objects.all()  # Fetch all tasks
    print("Tasks from DB:", task) 
    return render(request, 'tasks/task_list.html', {
        'task': task
    })

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()

    return render(request, 'tasks/create_task.html', {
        'form': form
    })
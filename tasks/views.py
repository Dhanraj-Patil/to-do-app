import json, requests

from django.shortcuts import render, redirect

from .models import Task, Project
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all().order_by('-created')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        

    context = {
        'tasks' : tasks,
        'form' : form
    }
    return render(request, 'tasks/index.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form' : form
    }
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {
        'task' : task
    }
    return render(request, 'tasks/delete.html', context)

def crossTask(request, pk):
    task = Task.objects.get(id=pk)
    task.complete = True
    task.save()
    return redirect('/')

def uncrossTask(request, pk):
    task = Task.objects.get(id=pk)
    task.complete = False
    task.save()
    return redirect('/')

def projects(request):
    context = {
        'projects' : Project.objects.all()
    }

    return render(request, 'tasks/projects.html', context)
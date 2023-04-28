from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, NewUserForm
from django.contrib import messages


def index(request, status):
    tasks = []
    if request.user.is_authenticated:
        if status == 'all':
            tasks = Task.objects.filter(user=request.user).order_by('-id')
        elif status == 'completed':
            tasks = Task.objects.filter(user=request.user, is_completed=True).order_by('-id')
        elif status == 'uncompleted':
            tasks = Task.objects.filter(user=request.user, is_completed=False).order_by('-id')

    return render(request, 'main/index.html', {'tasks': tasks})


def create(request):
    error = ''
    form = TaskForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save(user=request.user)
            return redirect('home')
        else:
            error = 'Not valid form'

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def delete_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    context = {'task': task}
    return render(request, 'main/delete_task.html', context)


def registration(request):
    form = NewUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('/')

    context = {'form': form}
    return render(request, 'registration/registration.html', context)

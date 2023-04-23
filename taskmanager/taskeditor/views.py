from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('-id')
        return render(request, 'main/index.html', {'tasks': tasks})
    else:
        return render(request, 'main/index.html')


def create(request):
    error = ''
    form = TaskForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save(user=request.user)
            return redirect('/')
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
        return redirect('/')

    context = {'task': task}
    return render(request, 'main/delete_task.html', context)

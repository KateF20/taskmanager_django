from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, NewUserForm
from django.contrib import messages


def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('-id')
        return render(request, 'main/index.html', {'title': 'Main page', 'tasks': tasks})
    else:
        return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    form = TaskForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save(user=request.user)
            return redirect('main')
        else:
            error = 'Not valid form'

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def registration(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('/')

    form = NewUserForm()

    context = {'form': form}
    return render(request, 'registration/registration.html', context)

from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Main page', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    # print(request.user)
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save(user=request.user)
            return redirect('home')
        else:
            error = 'Not valid form'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def home(request):
    return render(request, 'registration/home.html')

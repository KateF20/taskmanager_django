from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Task, Group
from .forms import TaskForm, NewUserForm, GroupForm
from django.contrib import messages
from django.views.decorators.http import require_http_methods


def index(request, status=None, group_id=None):
    tasks = []
    groups = Group.objects.filter(user=request.user)
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('-id')
        if status == 'all':
            pass
        elif status == 'completed':
            tasks = tasks.filter(is_completed=True)
        elif status is None:
            tasks = tasks.filter(is_completed=False)
        else:
            return HttpResponseNotFound('Page not found')

        if group_id is not None:
            if group_id.isdigit():
                tasks = tasks.filter(group_id=group_id)
            else:
                return HttpResponseNotFound('Page not found')

    context = {'tasks': tasks, 'groups': groups, 'status': status, 'group_id': group_id or ''}

    return render(request, 'main/index.html', context)


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


@require_http_methods(["POST"])
def check_completed(request, id):
    task = Task.objects.get(id=id)

    if request.POST.get('is_complete') == 'on':
        task.is_completed = True
    else:
        task.is_completed = False
    task.save()

    return HttpResponse()


def registration(request):
    form = NewUserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('/')

    context = {'form': form}
    return render(request, 'registration/registration.html', context)


def create_group(request):
    form = GroupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True, user=request.user)
            return redirect('home')

    return render(request, 'main/create_group.html', {'form': form})


def delete_group(request, id):
    group = Group.objects.get(id=id)

    if request.method == 'POST':
        group.delete()
        return redirect('home')

    context = {'group': group}
    return render(request, 'main/delete_group.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TodoForm
from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.all()
    form = TodoForm
    context = {
        'form': form,
        'todos': todos
    }
    return render(request, 'todo/index.html', context)


def create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')


def update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'todo': todo,
        'form': form
    }
    return render(request, 'todo/edit.html', context)


def delete(request, id):
    todo = Todo.objects.get(id=id)
    if todo:
        todo.delete()
    return redirect('home')


def mark_as_completed(request, id):
    todo = Todo.objects.get(id=id)
    todo.comleted = True
    todo.save()
    return redirect('home')

from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoForm

def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    todos = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todos': todos, 'form': form})

def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    return render(request, 'todo/delete_confirm.html', {'todo': todo})

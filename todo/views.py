from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm

def index(request):
	todo_list = Todo.objects.order_by('id')
	form = TodoForm()


	context = {'todo_list': todo_list, 'form': form}

	return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):

	form = TodoForm(request.POST)

	print(request.POST['text'])
	if form.is_valid():
		insert = Todo(text=request.POST['text'])
		insert.save()

	return redirect('index')

def completeTodo(request, todo_id):

	todo = Todo.objects.get(pk=todo_id)
	todo.completed=True
	todo.save()

	return redirect('index')


def deleteComplete(request):

	Todo.objects.filter(completed__exact=True).delete()

	return redirect('index')

def deleteAll(request):

	Todo.objects.all().delete()

	return redirect('index')
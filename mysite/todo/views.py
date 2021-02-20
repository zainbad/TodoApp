from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from . models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import CreateUserForm, todoForm, taskForm
from django.core import serializers
from . models import User_Profile

# Create your views here.
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			messages.success(request, 'Account was created for ' + username)

			return redirect('/')
		

	context = {'form':form}
	return render(request, 'todo/register.html', context)

def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'todo/login.html', context)


@login_required(login_url='/')
def home(request):

    context = {
        'todo_lists': Todo_list.objects.filter(user=request.user, ).order_by('-pk'),
        'form': todoForm(),

    }
    return render(request, 'todo/todo.html', context)


def list_tasks(request, pk):
    todo_list = Todo_list.objects.get(id=pk)
    tasks = Task.objects.filter(todo_list=todo_list, status='Pending')
    context = {
        "tasks": tasks,
        "list": todo_list,
        "form": taskForm(),
    }

    return render(request, 'todo/task.html', context)



def add_task(request, pk):
    if request.is_ajax and request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            instance = form.save()
            todolist = Todo_list.objects.get(id=pk)
            instance.todo_list = todolist
            instance.save()
            ser_instance = serializers.serialize('json', [instance,])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def add_list(request):
   # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = todoForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)


def done_task(request, pk):
    task = Task.objects.get(id=pk)
    task.status = 'Done'
    task.save()
    todo_id = task.todo_list.id
    return redirect('/todo/{}'.format(todo_id))


def done_task_ajax(request):
    if request.is_ajax and request.method == 'GET':
        task_id = int(request.GET.get('task_id', None))
        task = Task.objects.get(id = task_id)
        task.delete()

        return JsonResponse({'delete': True}, status=200)
    
    return JsonResponse({}, status=400)


def profile(request, pk):
    user = User.objects.get(id=pk)
    profile = User_Profile.objects.get(user=user)
    context = {
        "profile": profile,
    }

    return render(request, 'todo/profile.html', context)






def complete_task(request):
    tasks = Task.objects.filter(status='Done')
    context={
        "tasks": tasks,
        "count": Task.objects.filter(status='Done').count()
    }

    return render(request, 'todo/complete.html', context)



def delete_list(request, pk):
    list = Todo_list.objects.get(id=pk)
    tasks = Task.objects.filter(todo_list = list)
    context ={

        "list": list,
        "tasks": tasks,
    }

    return render(request, 'todo/delete_list.html', context)



def delete_list_done(request, pk):
    list = Todo_list.objects.get(id=pk)
    list.delete()

    return redirect(reverse('home'))

    


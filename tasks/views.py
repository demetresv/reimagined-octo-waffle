from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')



def create_task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your product has been created successfully.')
            return redirect('home')
    return render(request, 'task_form.html', {'form': form})

def update_task(request,pk):
    product = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=product)

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your product has been Updated successfully.')
            return redirect('task_detail', id=id)
    return render(request, 'task_form.html',{'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Product, pk=id)
    task.delete()
    messages.add_message(request, messages.SUCCESS, 'Your product has been deleted.')
    return redirect('home')

def detail_task(request, pk):
    product = get_object_or_404(Task, pk=id)
    return render(request, 'task_detail.html')



from django.shortcuts import redirect, render
from . models import Todo
from django.contrib import messages
from . forms import TodoForms
# Create your views here.
def home(request):
    task_list=Todo.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        date=request.POST.get('date')
        task=Todo(name=name,date=date)
        task.save()
    return render(request,'index.html',{'task_list':task_list})
def delete(request,task_id):
    task=Todo.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    messages.error(request,'Are you sure did you completed this task?')
    return render(request,'index.html')
def update(request,id):
    task=Todo.objects.get(id=id)
    form=TodoForms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})
        
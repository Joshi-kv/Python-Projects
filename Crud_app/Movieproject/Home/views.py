from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Movies
from .forms import Movieform
from django.contrib import messages

# Create your views here.
def home(request):
    movie=Movies.objects.all()
    return render(request,'index.html',{'movie_list':movie})

def detail(request,movie_id):
    details=Movies.objects.get(id=movie_id)
    return  render(request,'detail.html',{'movie':details})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        discription=request.POST.get('discription')
        year=request.POST.get('year')
        image=request.FILES['image']
        movie=Movies(name=name,discription=discription,year=year,image=image)
        movie.save()
        return redirect('Home:add_movie')
    return render(request,'add_movie.html')
def update(request,id):
    movie=Movies.objects.get(id=id)
    form=Movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    movie=Movies.objects.get(id=id)
    if request.method=='POST':
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

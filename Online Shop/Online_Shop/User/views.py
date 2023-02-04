from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
#fetching data from db to create user
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        
        
        #condition checking
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'Username already exists try another one')
                return redirect('User:signup')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'Email already registered')
                return redirect('User:signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('User:login')
        else:
            messages.error(request,'Password not matching please check.')
    return  render(request,'register.html')   

#login function
def login(request):
    if request.method=='POST':
   
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            messages.error(request,'Invalid credentials try again')
            return redirect('User:login')
    return render(request,'login.html')

#logout function
def logout(request):
    auth.logout(request)
    return redirect('Home:homepage')
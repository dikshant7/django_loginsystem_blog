from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method=='POST':
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        x=User.objects.create_user(username=username,email=email,password=password)
        x.save()
        print('user created succesfully')
        return redirect('/')
    else:
        return render(request,'signup.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['password']
        x=auth.authenticate(username=username,password=password)
        if x is not None:
            auth.login(request,x)
            return redirect('home')
        else:
            print('credentials invalid')
            return redirect('login')

    else:
            return render(request,'login.html')
        
            


@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if User.is_authenticated:
        return render(request,'home.html')
    else:
        redirect('/')


def logout(request):
    
    auth.logout(request)
    return redirect('/')
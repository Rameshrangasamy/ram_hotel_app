from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Menuitem
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def index(request):   
    
    lists = Menuitem.objects.all()
    
    return render(request, 'index.html', {'lists': lists})

def login(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
            
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save();
                print('user created')
                return redirect('login')                
            
        else:
            messages.info(request, "password not matching")
            return redirect('register')      
        
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
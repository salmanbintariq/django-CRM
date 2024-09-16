from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm
# Create your views here.

def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in !!")
            return redirect('main:home')
        else:
            messages.error(request,"Invalid username and password. Please Try again!")
            return redirect('main:home')
    else:
        return render(request, 'main/home.html')


def logout_user(request):
        logout(request)
        messages.success(request,"You have been logged out...!!")
        return redirect('main:home')
    
def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully registered !!")
            return redirect('main:home')
    else:
        form = SignupForm()    

    return render(request, 'main/register.html', {'form':form})  
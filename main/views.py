from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import SignupForm, RecordForm
from .models import Customer
# Create your views here.

def home(request):
    query = request.GET.get('q','')
    if query:
        customers = Customer.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(id__icontains=query) |
            Q(city__icontains=query)
        )
    else:    
        customers = Customer.objects.all()

    # Handle login logic    
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
        return render(request, 'main/home.html', {"customers":customers})

    
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


def customer_record(request,id):
    if request.user.is_authenticated:
        customer = get_object_or_404(Customer, id=id)
        return render(request, 'main/record.html', {"customer":customer})
    else:
        messages.error(request,"You must be logged in to view that page !!!")
        return redirect('main:home')
    
def delete_record(request,id):
    if request.user.is_authenticated:
        customer = get_object_or_404(Customer, id=id)
        customer.delete()
        messages.success(request,"Record deleted successfully !!!")
        return redirect('main:home')
    else:
        messages.error(request,"You must be logged in to that !!!")
        return redirect('main:home')

def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Record added successfully!")
                return redirect('main:home')
        else:
            form = RecordForm()    
        return render(request, 'main/add_record.html', {"form":form})
    else:
        messages.error(request,"You must be logged in to that !!!")
        return redirect('main:home')

def edit_record(request,id):
    if request.user.is_authenticated:
        customer = get_object_or_404(Customer,id=id)
        form = RecordForm(request.POST or None, instance=customer) # Use request.POST or None to handle both GET and POST
        if form.is_valid():
            form.save()
            messages.success(request,"Record updated successfully!")
            return redirect('main:home')
        return render(request, 'main/edit_record.html', {"form":form})
    else:
        messages.error(request,"You must be logged in to edit a record!")
        return redirect('main:home')        
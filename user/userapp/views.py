from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django . contrib import messages
from django . contrib.auth import login,logout,authenticate
from django . contrib. auth.models import User


# Create your views here.

def home(request):
    return render(request,'home.html')

def UserRegister(request):
    form = UserCreationForm()
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Registerd...')
            return redirect('home')
        else:
            messages.error(request,'oops.. Something Went Wrong')
            return redirect('UserRegister')

    context = {'form':form}
    return render(request,"UserRegister.html",context)

def UserLogin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'Login successfully ')
            return redirect('home')
        else:
            messages.error(request,'something went wrong')

    return render(request,"login.html")

def ConfirmLogout(request):
    logout(request)
    messages.success(request,"logout successfully")
    return redirect('Login')
        
def UserLogout(request):
    return render(request,"logoutconfirm.html")
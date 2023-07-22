from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from django.contrib import messages

@login_required(login_url='Login')
def home(request):
    form=TodoForm
    if request.method == 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.user=request.user
            user.task=user.task.capitalize()
            user.save()
            messages.success(request,"Created")
            return redirect('home')
    context={'form':form}
    return render(request,'home.html',context)

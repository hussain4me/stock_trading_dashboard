from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Trade, User
# Create your views here.


def user_login(request):
    

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user=User.objects.get(email=username)
        except:
            messages.error("User not exist")

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff and user.is_active:
                return redirect('admin_home')
            elif user.is_staff == False and user.is_active:
                return redirect('user_home')
    
    return render(request, 'login.html')

    
def user_logout(request):
    logout(request)

    return redirect("login")


@login_required(login_url='login')
def user_dashboard(request):
    user = request.user.id
    trades = Trade.objects.filter(user__id=user)
    context = {'trades': trades}
    return render(request, 'user/dashboard.html', context)

@login_required(login_url='login')
def admin_dashboard(request):
    # if not request.user.is_staff :
    trades = Trade.objects.filter()
    context = {'trades': trades}
    return render(request, 'admin/dashboard.html', context)
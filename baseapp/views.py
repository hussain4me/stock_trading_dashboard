from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
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
                return render(request, 'admin/dashboard.html')
            elif user.is_staff == False and user.is_active:
                return render(request, 'user/dashboard.html')
    
    return render(request, 'login2.html')

    
def user_logout(request):
    logout(request)

    return redirect("login")


@login_required(login_url='login')
def user_dashboard(request):
    request.auth.user
    # return HttpResponse("User dashboard")
    return render(request, 'user\dashboard.html')


@login_required(login_url='login')
def admin_dashboard(request):
    # return HttpResponse("Admin dashboard")
    return render(request, 'admin\dashboard.html')
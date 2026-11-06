from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from FlowerApp.models import Flower
from OrderApp.models import Order

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password!")

    return render(request, 'login.html')

@login_required(login_url='login')
def dashboard(request):
    context = {
        'total_flowers': Flower.objects.count(),
        'total_orders': Order.objects.count(),
    }
    return render(request, 'dashboard.html', context)

def about(request):
    return render(request, 'about.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Logout successfully!")
        return redirect('login')

    return redirect('dashboard')
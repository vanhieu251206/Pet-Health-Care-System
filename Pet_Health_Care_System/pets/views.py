from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Product

User = get_user_model()

# Create your views here.
def guest_dashboard(request):
    context = {}
    return render(request, 'pets/guest_dashboard.html', context)

def login_page(request):
    context = {}
    return render(request, 'pets/login_page.html', context)

def select_role(request):
    context = {}
    return render(request, 'pets/select_role.html', context)

def dashboard_customer(request):
    context = {}
    return render(request, 'pets/dashboard_customer.html', context)

def cart(request):
    context = {}
    return render(request, 'pets/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'pets/checkout.html', context)

def vaccination(request):
    context = {}
    return render(request, 'pets/vaccination.html', context)

def periodic_health_checkups(request):
    context = {}
    return render(request, 'pets/periodic_health_checkups.html', context)

def about_us(request):
    context ={}
    return render(request, 'pets/about_us.html', context)

def contact(request):
    context ={}
    return render(request, 'pets/contact.html', context)

def shop(request):
    products =  Product.objects.all()
    return render(request, 'pets/shop.html', {'products': products})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")  # Lấy vai trò từ form

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Điều hướng theo vai trò
            if role == "customer":
                return redirect("customer_dashboard")  
            elif role == "admin":
                return redirect("admin_dashboard") 
            elif role == "vet":
                return redirect("vet_dashboard")  
            elif role == "vet":
                return redirect("staff_dasboard") 
            else:
                return redirect("home")  
        else:
            return render(request, "pets/login_page.html", {"error": "Sai thông tin đăng nhập"})

    return render(request, "pets/login_page.html")




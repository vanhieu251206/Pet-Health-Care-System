from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Product
from staff.views import tong_quan

CustomUser = get_user_model()

# Create your views here.
def guest_dashboard(request):
    context = {}
    return render(request, 'pets/guest_dashboard.html', context)

def login_page(request):
    context = {}
    return render(request, 'pets/login_page.html', context)

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

def register_page(request):
    context ={}
    return render(request, 'pets/register_page.html', context)

def shop(request):
    products =  Product.objects.all()
    return render(request, 'pets/shop.html', {'products': products})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.role == role:  
                login(request, user)

                if role == "customer":
                    return redirect("staff:tong_quan")  
                elif role == "staff":
                    return redirect("staff:tong_quan")
                elif role == "doctor":
                    return redirect("staff:tong_quan")
                elif role == "admin":
                    return redirect("staff:tong_quan")
                else:
                    messages.error(request, "Vai trò không hợp lệ.")
                    return redirect("pets:login_page")
            else:
                messages.error(request, "Vai trò không khớp với tài khoản.")
                return redirect("pets:login_page")
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng.")
            return redirect("pets:login_page")
        
def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password_confirm = request.POST["password_confirm"]
        role = request.POST["role"]

        if password != password_confirm:
            messages.error(request, "Mật khẩu xác nhận không khớp.")
            return redirect("pets:register_views")

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Tên đăng nhập đã tồn tại.")
            return redirect("pets:register_view")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email đã được sử dụng.")
            return redirect("pets:register_view")

        user = CustomUser.objects.create_user(username=username, email=email, password=password, role=role)
        user.save()

        messages.success(request, "Đăng ký thành công! Vui lòng đăng nhập.")
        return redirect("pets:login_page")  

    return render(request, "pets/login_page.html")





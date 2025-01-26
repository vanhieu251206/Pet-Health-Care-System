from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Pet
from .serializers import PetSerializer

# Guest page view
def guest_page(request):
    return render(request, 'pets/guest_page.html')

# Login page view
def login_page(request):
    return render(request, 'pets/login_page.html')

# Role selection view
def select_role(request):
    return render(request, 'pets/select_role.html')

# Customer dashboard view
@login_required
def dashboard_customer(request):
    return render(request, 'pets/dashboard_customer.html')

# Shopping cart view
def cart(request):
    return render(request, 'pets/cart.html')

# Checkout page view
def checkout(request):
    return render(request, 'pets/checkout.html')

# Login processing view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')  # Role from form

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if the role matches the user's role
            if role == user.userprofile.role:
                login(request, user)
                if role == 'customer':
                    return redirect('customer_dashboard')
                elif role == 'staff':
                    return redirect('staff_dashboard')
                elif role == 'vet':
                    return redirect('vet_dashboard')
                elif role == 'admin':
                    return redirect('admin_dashboard')
            else:
                messages.error(request, "Tài khoản không phù hợp với vai trò đã chọn.")
        else:
            messages.error(request, "Sai tên đăng nhập hoặc mật khẩu.")
    return render(request, 'pets/login_page.html')

# Staff dashboard view
@login_required
def staff_dashboard(request):
    return render(request, 'pets/staff_dashboard.html')

# Role redirection view
def select_role_view(request):
    role = request.GET.get('role', None)
    if role == 'customer':
        return redirect('customer_dashboard')
    elif role == 'staff':
        return redirect('staff_dashboard')
    elif role == 'vet':
        return redirect('vet_dashboard')
    elif role == 'admin':
        return redirect('admin_dashboard')
    else:
        return HttpResponseBadRequest("Vai trò không hợp lệ.")

# About page view
def introduce(request):
    return render(request, 'pets/introduce.html')

# Contact page view
def contact_page(request):
    # Context không bị ràng buộc bởi role
    context = {
        "email": "GroupOne@gmail.com",
        "hotline": "+84 382 771 491",
        "address": "70 Tô Ký, Tân Chánh Hiệp, Quận 12, TP. HCM",
    }
    return render(request, 'pets/contact.html', context)


# API view for Pet model
class PetList(APIView):
    def get(self, request):  
        pets = Pet.objects.all()  
        serializer = PetSerializer(pets, many=True)  
        return Response(serializer.data)

    def post(self, request):  # Add a new pet
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

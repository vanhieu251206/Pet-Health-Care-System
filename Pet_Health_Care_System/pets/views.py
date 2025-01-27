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
    context ={}
    return render(request, 'pets/shop.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']  # Vai trò đã được gửi từ form

        # Xác thực người dùng
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Kiểm tra xem vai trò có đúng không
            if role == 'customer' and user.userprofile.role == 'customer':
                login(request, user)
                return redirect('customer_dashboard')  # Chuyển tới trang dành cho khách hàng
            elif role == 'staff' and user.userprofile.role == 'staff':
                login(request, user)
                return redirect('staff_dashboard')  # Chuyển tới trang dành cho nhân viên
            elif role == 'vet' and user.userprofile.role == 'vet':
                login(request, user)
                return redirect('vet_dashboard')  # Chuyển tới trang dành cho bác sĩ
            elif role == 'admin' and user.userprofile.role == 'admin':
                login(request, user)
                return redirect('admin_dashboard')  # Chuyển tới trang dành cho quản trị viên
            else:
                messages.error(request, "Tài khoản không phù hợp với vai trò đã chọn.")
        else:
            messages.error(request, "Sai tên đăng nhập hoặc mật khẩu.")

    return render(request, 'pets/login_page.html')

from django.contrib.auth.decorators import login_required

@login_required
def customer_dashboard(request):
    return render(request, 'pets/customer_dashboard.html')

@login_required
def staff_dashboard(request):
    return render(request, 'pets/staff_dashboard.html')

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

class PetList(APIView):
    queryset = Pet.objects.all()

    def get(self, request):  
        pets = Pet.objects.all()  
        serializer = PetSerializer(pets, many=True)  
        return Response(serializer.data) 
    
    def post(self, request):  # Thêm thú cưng mới
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Lưu thú cưng mới vào cơ sở dữ liệu
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Trả về thông tin thú cưng mới
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Trả về lỗi nếu dữ liệu không hợp lệ

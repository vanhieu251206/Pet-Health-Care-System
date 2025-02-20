from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomUserForm
from django.contrib import messages
from pets.models import CustomUser

def tong_quan(request):
    context = {}
    return render(request, 'QTV/tong_quan.html', context)

def quan_ly_tai_khoan(request):
    users = CustomUser.objects.all()
    return render(request, 'QTV/quan_ly_tai_khoan.html', {'users': users})

def cau_hinh(request):
    context = {}
    return render(request, 'QTV/cau_hinh.html', context)

def doanh_thu(request):
    context = {}
    return render(request, 'QTV/doanh_thu.html', context)

def add_account(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if not username or not email or not password or not role:
            return render(request, 'QTV/quan_ly_tai_khoan.html', {'error': 'Vui lòng nhập đầy đủ thông tin'})
        
        try:
            user = CustomUser.objects.create(
                username=username,
                email=email,
                password=password,
                role=role,
            )

            user.set_password(password)
            user.save()

            return redirect('QTV:quan_ly_tai_khoan')
    
        except Exception as e:
            return render(request, 'QTV/quan_ly_tai_khoan.html', {'error': f'Lỗi khi tạo tài khoản: {e}'})
        
    return render(request, 'QTV/quan_ly_tai_khoan.html')

def delete_account(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()
    messages.success(request, "Tài khoản đã được xóa thành công.")
    return redirect('QTV:quan_ly_tai_khoan')




        
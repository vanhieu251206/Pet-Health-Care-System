from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomUserForm
from django.contrib import messages

def tong_quan(request):
    context = {}
    return render(request, 'QTV/tong_quan.html', context)

def quan_ly_tai_khoan(request):
    context = {}
    return render(request, 'QTV/quan_ly_tai_khoan.html', context)

def add_account(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tạo tài khoản thành công!')
            return redirect('QTV:quan_ly_tai_khoan') 
        else:
            messages.error(request, 'Có lỗi xảy ra. Vui lòng thử lại.')
    else:
        form = CustomUserForm()

    return render(request, 'QTV/add_account.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomUserForm
from django.contrib import messages

def tong_quan(request):
    context = {}
    return render(request, 'QTV/tong_quan.html', context)

def quan_ly_tai_khoan(request):
    context = {}
    return render(request, 'QTV/quan_ly_tai_khoan.html', context)

def cau_hinh(request):
    context = {}
    return render(request, 'QTV/cau_hinh.html', context)

def doanh_thu(request):
    context = {}
    return render(request, 'QTV/doanh_thu.html', context)



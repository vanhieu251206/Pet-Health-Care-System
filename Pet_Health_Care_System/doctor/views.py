from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def tong_quan(request):
    context = {}
    return render(request,'doctor/tong_quan.html', context)

def lich_lam_viec(request):
    context = {}
    return render(request,'doctor/lich_lam_viec.html', context)

def ho_so_benh_an(request):
    context = {}
    return render(request,'doctor/ho_so_benh_an.html', context)




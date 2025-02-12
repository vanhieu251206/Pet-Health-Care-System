from django.shortcuts import render, get_object_or_404, redirect

def dashboard(request):
    context = {}
    return render(request, 'doctor/dashboard.html', context)

def lich(request):
    context = {}
    return render(request, 'doctor/lich.html', context)

def hoso(request):
    context = {}
    return render(request, 'doctor/hoso.html', context)

def theodoi(request):
    context = {}
    return render(request, 'doctor/theodoi.html', context)

def baocao(request):
    context = {}
    return render(request, 'doctor/baocao.html', context)

def setting(request):
    context = {}
    return render(request, 'doctor/setting.html', context)

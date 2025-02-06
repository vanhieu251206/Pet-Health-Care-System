from django.shortcuts import render, get_object_or_404, redirect

def lich_hen(request):
    context = {}
    return render(request, 'staff/lich_hen.html', context)

def tong_quan(request):
    context = {}
    return render(request, 'staff/tong_quan.html', context)

def phong_luu_tru(request):
    context = {}
    return render(request, 'staff/phong_luu_tru.html', context)

def booking(request):
    context = {}
    return render(request, 'staff/booking.html', context)

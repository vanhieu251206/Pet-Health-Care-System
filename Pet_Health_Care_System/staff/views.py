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

def theo_doi(request):
    context = {}
    return render(request, 'staff/theo_doi_thu_cung.html', context)

def sap_lich(request):
    context = {}
    return render(request, 'staff/sap_xep_lich.html', context)

def quan_ly_tai_khoan(request):
    context = {}
    return render(request, 'staff/quan_ly_tai_khoan.html', context)

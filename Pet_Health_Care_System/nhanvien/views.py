from django.shortcuts import render
from nhanvien import views

# Create your views here.
def page_nhanvien(request):
    context = {}
    return render(request, 'nhanvien/trangchunhanvien.html', context)
def quanlithucung(request):
    context = {}
    return render(request, 'nhanvien/quanlithucung.html', context)

def trangchunhanvien(request):
    return render(request, 'nhanvien/trangchunhanvien.html')
def quanlilich(request):
    context = {}
    return render(request, 'nhanvien/quanlilich.html', context)
  
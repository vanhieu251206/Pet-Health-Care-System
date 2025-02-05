from django.shortcuts import render
from django.http import HttpResponse

from pets.models import Pet 

def staff_dashboard(request):
    context = {}
    return render(request, 'staff/staff_dashboard.html', context)

def quanlilich(request):
    context = {}
    return render(request, 'staff/quanlilich.html', context)

def hoadon(request):
    context = {}
    return render(request, 'staff/hoadon.html', context)
    
def quanlithucung(request):
    Pets = Pet.objects.all()
    context = {'Pets': Pets}
    return render(request, 'staff/quanlithucung.html', context)








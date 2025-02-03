from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def infor_view(request):
    return render(request, 'infor_view.html')

def update(request):
    return render(request, 'update.html')

def Calendar_doctor(request):
    return render(request, 'Calendar_doctor.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def base1(request):
    return render(request, 'staff/base1.html')  # Hiển thị giao diện base1

def Manage_cancellations(request):
    return render(request, 'staff/Manage_cancellations.html')

def Manage_Doctor(request):
    return render(request, 'staff/Manage_Doctor.html')

def update_pet(request):
    return render(request, 'staff/update_pet.html')



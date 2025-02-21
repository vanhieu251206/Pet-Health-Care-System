from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from pets.models import Appointment, CustomUser

def tong_quan(request):
    context = {}
    return render(request,'doctor/tong_quan.html', context)

def lich_lam_viec(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = CustomUser.objects.get(id=user_id)

        appointments = Appointment.objects.filter(doctor=user.full_name, status='confirmed')
    return render(request, 'doctor/lich_lam_viec.html', {"appointments": appointments})

def ho_so_benh_an(request):
    context = {}
    return render(request,'doctor/ho_so_benh_an.html', context)




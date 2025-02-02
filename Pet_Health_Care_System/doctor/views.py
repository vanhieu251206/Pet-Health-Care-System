from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Chào mừng đến với trang quản lý bác sĩ!")

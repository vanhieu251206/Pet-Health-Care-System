# doctor/views.py
from django.shortcuts import render

def dashboard(request):
    return render(request, 'doctor/dashboard.html')  # Đảm bảo template đúng

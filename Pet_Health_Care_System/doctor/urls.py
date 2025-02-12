from django.urls import path
from . import views

app_name = 'doctor'  # Đăng ký namespace cho ứng dụng 'doctor'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]

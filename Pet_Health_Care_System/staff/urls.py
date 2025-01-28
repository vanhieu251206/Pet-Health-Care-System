from django.urls import path
from . import views

urlpatterns = [
    path('', views.base1, name='base1'),  # Trang mặc định của staff
    path('Manage_cancellations/', views.Manage_cancellations, name='Manage_cancellations'),  # Liên kết lịch hủy
    path('Manage_Doctor/', views.Manage_Doctor, name='Manage_Doctor'),  # Liên kết lịch làm
]

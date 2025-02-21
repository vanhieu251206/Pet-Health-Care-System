from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = "doctor"

urlpatterns = [
    path('', lambda request: redirect('tong_quan/')),
    path('tong_quan/', views.tong_quan, name = "tong_quan"),
    path('lich_lam_viec/', views.lich_lam_viec, name = "lich_lam_viec"),
    path('ho_so_benh_an/', views.ho_so_benh_an, name = "ho_so_benh_an"),
    path('quan_ly_tai_khoan/', views.quan_ly_tai_khoan, name = "quan_ly_tai_khoan"),
]
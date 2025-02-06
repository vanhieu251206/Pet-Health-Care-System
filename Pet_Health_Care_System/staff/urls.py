from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('tong_quan/')),
    path('tong_quan/', views.tong_quan, name = "tong_quan"),
    path('phong_luu_tru/', views.phong_luu_tru, name = "phong_luu_tru"),
    path('lich_hen/', views.lich_hen, name = "lich_hen"),
    path('booking/', views.booking, name = "booking"),
]
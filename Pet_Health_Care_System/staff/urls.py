from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.staff_dashboard, name = "staff_dashboard"),
    path('quanlilich/', views.quanlilich, name = "quanlilich"),
    path('quanlithucung/', views.quanlithucung, name = "quanlithucung"),
    path('hoadon/', views.hoadon, name = "hoadon"),
]

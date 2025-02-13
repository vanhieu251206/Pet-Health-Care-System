from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = "QTV"

urlpatterns = [
    path('', lambda request: redirect('tong_quan/')),
    path('tong_quan/', views.tong_quan, name = "tong_quan"),
    path('quan_ly_tai_khoan/', views.quan_ly_tai_khoan, name = "quan_ly_tai_khoan"),
    path('add_account/', views.add_account, name='add_account'),
]
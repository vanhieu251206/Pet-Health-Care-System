from django.urls import path
from django.shortcuts import redirect
from . import views
from .views import add_account, delete_account

app_name = "QTV"

urlpatterns = [
    path('', lambda request: redirect('tong_quan/')),
    path('tong_quan/', views.tong_quan, name = "tong_quan"),
    path('quan_ly_tai_khoan/', views.quan_ly_tai_khoan, name = "quan_ly_tai_khoan"),
    path('cau_hinh/', views.cau_hinh, name = "cau_hinh"),
    path('doanh_thu/', views.doanh_thu, name = "doanh_thu"),
    path('add_account/', add_account, name = 'add_account'),
    path('delete_account/<int:user_id>/', delete_account, name = 'delete_account'),
]
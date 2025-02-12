from django.urls import path
from . import views

app_name = 'doctor'  # Đăng ký namespace cho ứng dụng 'doctor'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('lich/', views.lich, name='lich'),
    path('hoso/', views.hoso, name='hoso'),
    path('theodoi/', views.theodoi, name='theodoi'),
    path('baocao/', views.baocao, name='baocao'),
    path('setting/', views.setting, name='setting'),
]

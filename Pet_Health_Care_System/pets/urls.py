from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # Chuyển hướng từ '/' đến '/index/'
    path('', lambda request: redirect('index'), name='home'),

    # Đường dẫn trang chủ
    path('index/', views.index, name='index'),

    # Đường dẫn trang đăng nhập
    path('login/', views.login, name='login'),  # Đổi tên view login để tránh xung đột

    # Đường dẫn quên mật khẩu
    path('quenmk/', views.quenmk, name='quenmk'),  # Đổi tên view quenmk để dễ hiểu

    # Đường dẫn giới thiệu
    path('gioithieu/', views.gioithieu, name='gioithieu'),

     # Đường dẫn đăng kí
    path('dangki/', views.dangki, name='dangki'),

    # Đường dẫn lien he
    path('lienhe/', views.lienhe, name='lienhe'),

    # Đường dẫn dich vu
    path('dichvu/', views.dichvu, name='dichvu'), 

    # Đường dẫn mua sam
    path('muasam/', views.muasam, name='muasam'),

    # Đường dẫn kham benh
    path('dichvukhambenh/', views.dichvukhambenh, name='dichvukhambenh'),

    # Đường dẫn spa
    path('spa/', views.spa, name='spa'),
]

from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.guest_page, name = "guest_page"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('login_page/', views.login_page, name="login_page"),
    path('select_role/', views.select_role, name="select_role"),
    path('api/pets/', PetList.as_view(), name='pet-list'),
    path('select_role_view/', views.select_role_view, name='select_role_view'), 
    path('dashboard_customer/', views.dashboard_customer, name='customer_dashboard'),
    path('login_view/', views.login_view, name="login_view")
    path('dog_products/', views.dog_products, name='dog_products'),
    #path('dashboard/staff/', views.dashboard_staff, name='staff_dashboard'),
    #path('dashboard/vet/', views.dashboard_vet, name='vet_dashboard'),
    #path('dashboard/admin/', views.dashboard_admin, name='admin_dashboard'),
    #path('dashboard_customer/', views.dashboard_customer, name="dashboard_customer"),
=======
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

     # Đường dẫn dat lich
    path('datlich/', views.datlich, name='datlich'),
>>>>>>> ca318054cb536b5f1be4088af93423818228af37
]

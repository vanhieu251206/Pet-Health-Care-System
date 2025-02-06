from django.urls import path
from . import views
from django.shortcuts import redirect
from .views import login_view

urlpatterns = [
    path('', lambda request: redirect('guest_dashboard/')),
    path('guest_dashboard/', views.guest_dashboard, name = "guest_dashboard"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('login_page/', views.login_page, name="login_page"),
    path('select_role/', views.select_role, name="select_role"),
    path('dashboard_customer/', views.dashboard_customer, name='customer_dashboard'),
    path('vaccination/', views.vaccination, name="vaccination"),
    path('periodic_health_checkups/', views.periodic_health_checkups, name="periodic_health_checkups"),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path("login/", login_view, name="login_view"),
    #path('dashboard/staff/', views.dashboard_staff, name='staff_dashboard'),
    #path('dashboard/vet/', views.dashboard_vet, name='vet_dashboard'),
    #path('dashboard/admin/', views.dashboard_admin, name='admin_dashboard'),
    #path('dashboard_customer/', views.dashboard_customer, name="dashboard_customer"),
]
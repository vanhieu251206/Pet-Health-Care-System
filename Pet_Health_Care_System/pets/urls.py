from django.urls import path,include
from . import views
from .views import PetList

urlpatterns = [
    path('', views.guest_page, name = "guest_page"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('login_page/', views.login_page, name="login_page"),
    path('select_role/', views.select_role, name="select_role"),
    path('api/pets/', PetList.as_view(), name='pet-list'),
    path('select_role_view/', views.select_role_view, name='select_role_view'), 
    path('dashboard_customer/', views.dashboard_customer, name='customer_dashboard'),
    path('login_view/', views.login_view, name="login_view")
    #path('dashboard/staff/', views.dashboard_staff, name='staff_dashboard'),
    #path('dashboard/vet/', views.dashboard_vet, name='vet_dashboard'),
    #path('dashboard/admin/', views.dashboard_admin, name='admin_dashboard'),
    #path('dashboard_customer/', views.dashboard_customer, name="dashboard_customer"),
]
from django.urls import path
from . import views
from django.shortcuts import redirect
from .views import register_view, login_view, cart_view, add_to_cart, remove_from_cart, update_cart
from django.contrib.auth import views as auth_views

app_name = "pets"

urlpatterns = [
    path('', lambda request: redirect('guest_dashboard/')),
    path('guest_dashboard/', views.guest_dashboard, name = "guest_dashboard"),
    path('cart/', cart_view, name="cart_view"),
    path('checkout/', views.checkout, name="checkout"),
    path('login_page/', views.login_page, name="login_page"),
    path('register_page/', views.register_page, name="register_page"),
    path('dashboard_customer/', views.dashboard_customer, name='customer_dashboard'),
    path('vaccination/', views.vaccination, name="vaccination"),
    path('periodic_health_checkups/', views.periodic_health_checkups, name="periodic_health_checkups"),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path("login/", login_view, name="login_view"),
    path("register/", register_view, name="register_view"),
    path('logout/', auth_views.LogoutView.as_view(next_page='pets:login_page'), name='logout'),
    path("add_to_cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<int:item_id>/", remove_from_cart, name="remove_from_cart"),
    path('update_cart/<int:item_id>/', update_cart, name="update_cart"),
]
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.guest_page, name = "guest_page"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('login_page/', views.login_page, name="login_page"),
]
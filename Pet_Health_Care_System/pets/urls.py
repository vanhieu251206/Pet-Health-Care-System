from django.urls import path,include
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('index/')),
    path('index/', views.index, name = "index"),
    path('login/', views.login, name = "login"),
    path('quenmk/', views.quenmk, name = "quenmk"),
]
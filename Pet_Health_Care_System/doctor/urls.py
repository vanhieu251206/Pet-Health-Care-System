from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('infor_view/', views.infor_view, name='infor_view'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/', views.update, name='update'),
    path('Calendar_doctor/', views.Calendar_doctor, name='Calendar_doctor'),
    path('infor_view/', views.infor_view, name='infor_view'),
]

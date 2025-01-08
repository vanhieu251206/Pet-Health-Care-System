from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.guest_page, name = "guest_page"),
]
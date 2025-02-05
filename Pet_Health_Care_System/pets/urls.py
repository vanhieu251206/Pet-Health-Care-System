from django.urls import path,include
from django.shortcuts import redirect
from . import views
from .views import PetViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'pets', PetViewSet)

urlpatterns = [
    path('', lambda request: redirect('guest_dashboard/')),
    path('guest_dashboard/', views.guest_dashboard, name = "guest_dashboard"),
    path('login/', views.login, name = "login"),
    path('quenmk/', views.quenmk, name = "quenmk"),

]
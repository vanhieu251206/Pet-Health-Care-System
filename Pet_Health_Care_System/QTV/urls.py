from django.urls import path
from . import views

app_name = 'QTV'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Đường dẫn gốc trỏ đến view dashboard
    # Các URL khác trong ứng dụng QTV
    path('QL/', views.QL, name='QL'),
    path('CH/', views.CH, name='CH'),
    path('BC/', views.BC, name='BC'),
]

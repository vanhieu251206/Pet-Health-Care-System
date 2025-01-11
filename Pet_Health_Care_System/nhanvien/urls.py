from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_nhanvien, name='page_nhanvien'),
    path('trangchunhanvien/quanlithucung.html', views.quanlithucung, name='quanlithucung_html'),
    path('trangchunhanvien/', views.trangchunhanvien, name='trangchunhanvien'),
    path('trangchunhanvien/quanlilich/', views.quanlilich, name='quanlilich'),
]

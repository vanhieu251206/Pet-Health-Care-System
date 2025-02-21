from django.urls import path
from django.shortcuts import redirect
from . import views
from .views import product_list

app_name = "staff"

urlpatterns = [
    path('', lambda request: redirect('tong_quan/')),
    path('tong_quan/', views.tong_quan, name = "tong_quan"),
    path('phong_luu_tru/', views.phong_luu_tru, name='phong_luu_tru'),
    path('lich_hen/', views.lich_hen, name = "lich_hen"),
    path('booking/', views.booking, name = "booking"),
    path('theo_doi/', views.theo_doi, name = "theo_doi"),
    path('sap_lich/', views.sap_lich, name = "sap_lich"),
    path('quan_ly_tai_khoan/', views.quan_ly_tai_khoan, name = "quan_ly_tai_khoan"),
    path('quan_ly_san_pham/', product_list, name='quan_ly_san_pham'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/update/<int:appointment_id>/', views.update_appointment_status, name='update_appointment_status'),
    path('add_room/', views.add_room, name = "add_room"),
    path('enter_room/', views.enter_room, name = "enter_room"),
    path('booking/confirm/<int:booking_id>/', views.confirm_booking, name='confirm_booking'),
    path('booking/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
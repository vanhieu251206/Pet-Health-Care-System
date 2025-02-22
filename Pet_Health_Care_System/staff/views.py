from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from pets.models import Product, Appointment
from .models import Room
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def lich_hen(request):
    context = {}
    return render(request, 'staff/lich_hen.html', context)

def tong_quan(request):
    context = {}
    return render(request, 'staff/tong_quan.html', context)

def booking(request):
    bookings = Appointment.objects.filter(service="Lưu trú")
    return render(request, 'staff/booking.html', {"bookings": bookings})

def theo_doi(request):
    context = {}
    return render(request, 'staff/theo_doi_thu_cung.html', context)

def sap_lich(request):
    context = {}
    return render(request, 'staff/sap_xep_lich.html', context)

def quan_ly_tai_khoan(request):
    context = {}
    return render(request, 'staff/quan_ly_tai_khoan.html', context)

def product_list(request):
    products = Product.objects.all()
    return render(request, 'staff/quan_ly_san_pham.html', {'products': products})

def appointment_list(request):
    appointments = Appointment.objects.exclude(service="Lưu trú")  
    return render(request, 'staff/lich_hen.html', {'appointments': appointments})

def update_appointment_status(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['Pending', 'Confirmed', 'Completed', 'Cancelled']:
            appointment.status = new_status
            appointment.save()
            messages.success(request, f"Lịch hẹn đã được cập nhật thành công.")
        else:
            messages.error(request, 'Trạng thái không hợp lệ.')

    return redirect('staff:appointment_list')  

def phong_luu_tru(request):
    rooms = Room.objects.all()
    available_rooms =  Room.objects.filter(status='available')
    return render(request, 'staff/phong_luu_tru.html', {'rooms': rooms, 'available_rooms': available_rooms})

def add_room(request):
    if request.method == 'POST':
        room_code = request.POST.get('room_code') 
        if Room.objects.filter(room_code=room_code).exists():
            return render(request, 'staff/phong_luu_tru.html', {'error': 'Mã chuồng đã tồn tại'})
        else:
            new_room = Room(room_code=room_code)
            new_room.save()
            return redirect('staff:phong_luu_tru') 

    return render(request, 'staff/phong_luu_tru.html')  

def enter_room(request):
    available_rooms = Room.objects.filter(status='available')
    
    if request.method == 'POST':
        room_code = request.POST.get('room_code')
        owner_name = request.POST.get('owner_name')
        pet_name = request.POST.get('pet_name')
        check_in_date = request.POST.get('check_in_date')
        expected_check_out_date = request.POST.get('expected_check_out_date')

        try:
            room = Room.objects.get(room_code=room_code)
            room.owner_name = owner_name
            room.pet_name = pet_name
            room.check_in_date = check_in_date
            room.expected_check_out_date = expected_check_out_date
            room.status = 'booked'  
            room.save()

            return redirect('staff:phong_luu_tru') 
        except Room.DoesNotExist:
            return render(request, 'staff/phong_luu_tru.html', {'error': 'Mã chuồng không tồn tại'})

    return render(request, 'staff/phong_luu_tru.html', {'available_rooms': available_rooms})

@csrf_exempt
def confirm_booking(request, booking_id):
    if request.method == 'POST':
        try:
            booking = Appointment.objects.get(id=booking_id)
            booking.status = 'Confirmed' 
            booking.save()

            return redirect('staff:booking') 
        except Appointment.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Booking not found'})

@csrf_exempt
def cancel_booking(request, booking_id):
    if request.method == 'POST':
        try:
            booking = Appointment.objects.get(id=booking_id)
            booking.status = 'Cancelled' 
            booking.save()

            return redirect('staff:booking')  
        except Appointment.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Booking not found'})
        
def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        if name and price and image:
            product = Product(name=name, price=price, image=image)
            product.save()
            return redirect('staff:quan_ly_san_pham')

    return render(request, 'staff/add_product.html')


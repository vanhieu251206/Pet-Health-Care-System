from django.shortcuts import render, get_object_or_404, redirect
from pets.models import Product, Appointment
from django.contrib import messages

def lich_hen(request):
    context = {}
    return render(request, 'staff/lich_hen.html', context)

def tong_quan(request):
    context = {}
    return render(request, 'staff/tong_quan.html', context)

def phong_luu_tru(request):
    context = {}
    return render(request, 'staff/phong_luu_tru.html', context)

def booking(request):
    context = {}
    return render(request, 'staff/booking.html', context)

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
    appointments = Appointment.objects.all()  
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
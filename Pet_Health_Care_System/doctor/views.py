from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointment, Pet, WorkSchedule

# Dashboard (Tổng quan)
def dashboard(request):
    context = {}
    return render(request, 'doctor/dashboard.html', context)

# Lịch làm việc của bác sĩ
def lich(request):
    appointments = Appointment.objects.all()  # Lấy tất cả các cuộc hẹn
    context = {'appointments': appointments}
    return render(request, 'doctor/lich.html', context)

# Hồ sơ bệnh án
def hoso(request):
    context = {}
    return render(request, 'doctor/hoso.html', context)

# Theo dõi tình trạng bệnh của thú cưng
def theodoi(request):
    context = {}
    return render(request, 'doctor/theodoi.html', context)

# Báo cáo và thống kê
def baocao(request):
    context = {}
    return render(request, 'doctor/baocao.html', context)

# Cài đặt và quản lý tài khoản bác sĩ
def setting(request):
    context = {}
    return render(request, 'doctor/setting.html', context)

# Danh sách cuộc hẹn
def appointment_list(request):
    appointments = Appointment.objects.all()  # Lấy tất cả các cuộc hẹn
    context = {'appointments': appointments}
    return render(request, 'doctor/appointment_list.html', context)

# Chi tiết hồ sơ bệnh án thú cưng
def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'doctor/pet_details.html', {'pet': pet})

# Xác nhận cuộc hẹn
def confirm_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    
    if request.method == "POST" and appointment.status != 'Confirmed':
        appointment.status = 'Confirmed'
        appointment.confirm_appointment()  # Cập nhật lịch làm việc của bác sĩ
        appointment.save()

        # Sau khi xác nhận, chuyển hướng về trang xác nhận
        return redirect('doctor:appointment_confirmed', appointment_id=appointment.id)
    
    return render(request, 'doctor/appointment_confirm.html', {'appointment': appointment})

# Trang xác nhận cuộc hẹn thành công
def appointment_confirmed(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'doctor/appointment_confirmed.html', {'appointment': appointment})

from django.contrib import admin
from .models import CustomUser, Pet, Appointment, WorkSchedule

# Tạo lớp quản trị cho CustomUser
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'phone', 'avatar')  # Các trường hiển thị trong admin
    search_fields = ('username', 'email')  # Thêm khả năng tìm kiếm qua username và email
    list_filter = ('role',)  # Thêm lọc theo vai trò (customer, doctor, admin, etc.)
    ordering = ('username',)  # Sắp xếp theo username

# Đăng ký CustomUser vào admin
admin.site.register(CustomUser, CustomUserAdmin)

# Tạo lớp quản trị cho Pet
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'owner_name', 'treatment_status', 'admission_reason')  # Các trường hiển thị trong admin
    search_fields = ('name', 'owner_name')  # Tìm kiếm qua tên thú cưng và chủ sở hữu
    list_filter = ('type', 'treatment_status')  # Lọc theo loại thú cưng và trạng thái điều trị
    ordering = ('name',)  # Sắp xếp theo tên thú cưng

# Đăng ký Pet vào admin
admin.site.register(Pet, PetAdmin)

# Tạo lớp quản trị cho Appointment
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'pet', 'doctor', 'date', 'time', 'status')  # Các trường hiển thị trong admin
    search_fields = ('name', 'pet__name', 'doctor__username')  # Tìm kiếm qua tên người và thú cưng
    list_filter = ('status', 'date', 'doctor')  # Lọc theo trạng thái, ngày và bác sĩ
    ordering = ('-date',)  # Sắp xếp theo ngày giảm dần

# Đăng ký Appointment vào admin
admin.site.register(Appointment, AppointmentAdmin)

# Tạo lớp quản trị cho WorkSchedule
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'pet', 'service', 'date', 'time')  # Các trường hiển thị trong admin
    search_fields = ('doctor__username', 'pet__name')  # Tìm kiếm qua tên bác sĩ và thú cưng
    list_filter = ('date', 'doctor')  # Lọc theo ngày và bác sĩ
    ordering = ('date', 'time')  # Sắp xếp theo ngày và giờ làm việc

# Đăng ký WorkSchedule vào admin
admin.site.register(WorkSchedule, WorkScheduleAdmin)

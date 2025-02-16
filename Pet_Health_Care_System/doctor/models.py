from django.db import models
from django.contrib.auth.models import AbstractUser

# Mô hình người dùng (CustomUser) với các quyền vai trò
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Khách'),
        ('staff', 'Nhân viên'),
        ('doctor', 'Bác sĩ'),
        ('admin', 'Admin'),
    )
    phone = models.CharField(max_length=10, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    def __str__(self):
        return self.username

# Mô hình Pet
class Pet(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)  # Chó, Mèo, Khác
    owner_name = models.CharField(max_length=255)
    owner_phone = models.CharField(max_length=15)
    admission_reason = models.CharField(max_length=255)
    treatment_status = models.CharField(
        max_length=20,
        choices=[('In Treatment', 'Đang điều trị'), ('Recovered', 'Đã hồi phục')],
        default='In Treatment'
    )

    def __str__(self):
        return self.name

# Mô hình Appointment (Cuộc hẹn)
class Appointment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Chủ sở hữu thú cưng
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)  # Liên kết với thú cưng
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    doctor = models.ForeignKey(CustomUser, related_name="appointments", on_delete=models.CASCADE)  # Bác sĩ phụ trách
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Chờ xác nhận'), ('Confirmed', 'Đã xác nhận'),
                 ('Completed', 'Đã hoàn thành'), ('Cancelled', 'Hủy')],
        default='Pending'
    )

    def __str__(self):
        return f"Lịch hẹn cho {self.name} vào ngày {self.date} lúc {self.time}"
    
    def confirm_appointment(self):
        """
        Phương thức xác nhận cuộc hẹn, tạo lịch làm việc cho bác sĩ.
        """
        if self.status == 'Confirmed':
            # Kiểm tra nếu lịch làm việc của bác sĩ đã có, nếu chưa tạo mới
            existing_schedule = WorkSchedule.objects.filter(
                doctor=self.doctor,
                pet=self.pet,
                date=self.date,
                time=self.time
            )

            if not existing_schedule.exists():
                # Tạo lịch làm việc mới cho bác sĩ
                self.doctor.schedule_set.create(
                    pet=self.pet,
                    service=self.service,
                    date=self.date,
                    time=self.time
                )
            self.save()

# Mô hình WorkSchedule (Lịch làm việc của bác sĩ)
class WorkSchedule(models.Model):
    doctor = models.ForeignKey(CustomUser, related_name="schedule_set", on_delete=models.CASCADE)  # Bác sĩ
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)  # Thú cưng
    service = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Lịch làm việc của {self.doctor.username} - {self.pet.name} vào ngày {self.date} lúc {self.time}"

from django.contrib.auth.models import AbstractUser
from django.db import models

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

# Mô hình Product (Sản phẩm)
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

# Mô hình Cart (Giỏ hàng)
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Giỏ hàng của {self.user.username}"

# Mô hình CartItem (Sản phẩm trong giỏ hàng)
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name} trong giỏ hàng của {self.cart.user.username}"

# Mô hình Appointment (Cuộc hẹn)
class Appointment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Liên kết với người dùng
    pet_name = models.CharField(max_length=100)  # Tên thú cưng
    pet_type = models.CharField(max_length=100)  # Loại thú cưng (Chó, Mèo, Khác)
    owner_name = models.CharField(max_length=100)  # Tên chủ thú cưng
    owner_phone = models.CharField(max_length=15)  # Số điện thoại chủ thú cưng
    date = models.DateField()  # Ngày hẹn
    time = models.TimeField()  # Giờ hẹn
    service = models.CharField(max_length=100)  # Dịch vụ yêu cầu
    branch = models.CharField(max_length=100)  # Chi nhánh
    doctor = models.ForeignKey(CustomUser, related_name='appointments', on_delete=models.CASCADE)  # Bác sĩ phụ trách
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Chờ xác nhận'), ('Confirmed', 'Đã xác nhận'),
                 ('Completed', 'Đã hoàn thành'), ('Cancelled', 'Hủy')],
        default='Pending'
    )

    def __str__(self):
        return f"Lịch hẹn cho {self.pet_name} vào ngày {self.date} lúc {self.time}"

    def confirm_appointment(self):
        """
        Phương thức xác nhận cuộc hẹn, tạo lịch làm việc cho bác sĩ.
        """
        if self.status == 'Confirmed':
            # Kiểm tra nếu lịch làm việc của bác sĩ đã có, nếu chưa tạo mới
            existing_schedule = WorkSchedule.objects.filter(
                doctor=self.doctor,
                pet_name=self.pet_name,
                date=self.date,
                time=self.time
            )

            if not existing_schedule.exists():
                # Tạo lịch làm việc mới cho bác sĩ
                self.doctor.schedule_set.create(
                    pet_name=self.pet_name,
                    service=self.service,
                    date=self.date,
                    time=self.time
                )
            self.save()

# Mô hình WorkSchedule (Lịch làm việc của bác sĩ)
class WorkSchedule(models.Model):
    doctor = models.ForeignKey(CustomUser, related_name="schedule_set", on_delete=models.CASCADE)  # Bác sĩ
    pet_name = models.CharField(max_length=100)  # Tên thú cưng
    service = models.CharField(max_length=100)  # Dịch vụ
    date = models.DateField()  # Ngày
    time = models.TimeField()  # Giờ

    def __str__(self):
        return f"Lịch làm việc của {self.doctor.username} - {self.pet_name} vào ngày {self.date} lúc {self.time}"

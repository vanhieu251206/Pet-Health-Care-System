from django.contrib.auth.models import AbstractUser
from django.db import models

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

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Giỏ hàng của {self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} trong giỏ hàng của {self.cart.user.username}"
    
from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)  
    phone = models.CharField(max_length=15)  
    date = models.DateField()  
    time = models.TimeField()  
    service = models.CharField(max_length=100) 
    branch = models.CharField(max_length=100)   
    doctor = models.CharField(max_length=100)  
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Chờ xác nhận'), ('Confirmed', 'Đã xác nhận'), 
                 ('Completed', 'Đã hoàn thành'), ('Cancelled', 'Hủy')],
        default='Pending'
    )

    def __str__(self):
        return f"Lịch hẹn cho {self.name} vào ngày {self.date} lúc {self.time}"


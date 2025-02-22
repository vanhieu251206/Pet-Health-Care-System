from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Khách'),
        ('staff', 'Nhân viên'),
        ('doctor', 'Bác sĩ'),
        ('admin', 'Admin'),
    )
    full_name = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True) 
    phone = models.CharField(max_length=10, blank=True, null=True) 
    email = models.EmailField(blank=True, null=True)  
    address = models.TextField(blank=True, null=True)  
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

class Appointment(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="appointments", null=True, blank=True)
    booked_by = models.CharField(max_length=255, null=True, blank=True)  
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Chờ xác nhận'), ('Confirmed', 'Đã xác nhận'), ('Cancelled', 'Hủy')],
        default='Pending'
    )

    def __str__(self):
        return f"Lịch hẹn của {self.customer.full_name} vào {self.date} lúc {self.time}"

class Pet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="pets")
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    species = models.CharField(
        max_length=100,
        choices=[('cat', 'Mèo'), ('dog', 'Chó')],
        default='cat'  
    )

    def __str__(self):
        return self.name
    
class Address(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user_address')  
    full_name = models.CharField(max_length=255)  
    phone = models.CharField(max_length=15)  
    street_address = models.CharField(max_length=255)  
    city = models.CharField(max_length=100)  
    district = models.CharField(max_length=100)  
    province = models.CharField(max_length=100)  
    
    def __str__(self):
        return f"{self.full_name} - {self.street_address}, {self.city}, {self.province}"

    class Meta:
        verbose_name = 'Địa chỉ'
        verbose_name_plural = 'Địa chỉ'

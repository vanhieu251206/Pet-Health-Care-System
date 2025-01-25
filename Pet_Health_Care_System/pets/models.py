from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('guest', 'Guest'),
        ('customer', 'Customer'),
        ('staff', 'Staff'),
        ('vet', 'Veterinarian'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(
        max_length = 20,
        choices=USER_TYPE_CHOICES,
        default='guest',
    )

    groups = models.ManyToManyField(
        Group,
        related_name='pets_user_groups',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='pet_user_permission',
        blank=True
    )

from django.db import models

class PetProduct(models.Model):
    name = models.CharField(max_length=255)  # Tên sản phẩm
    description = models.TextField()  # Mô tả sản phẩm
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Giá sản phẩm
    image = models.ImageField(upload_to='products/')  # Hình ảnh sản phẩm

    def __str__(self):
        return self.name



     
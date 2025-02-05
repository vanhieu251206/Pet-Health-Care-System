from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=255)  # Tên nhân viên
    age = models.IntegerField()  # Tuổi
    contact_info = models.CharField(max_length=255)  # Thông tin liên lạc (số điện thoại, email, v.v)
    working_hours = models.CharField(max_length=255)  # Giờ làm việc, ví dụ: "9:00 AM - 6:00 PM"
    
    def __str__(self):
        return self.name
    

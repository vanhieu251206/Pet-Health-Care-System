from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=255)  # Tên nhân viên
    age = models.IntegerField()  # Tuổi
    contact_info = models.CharField(max_length=255)  # Thông tin liên lạc (số điện thoại, email, v.v)
    working_hours = models.CharField(max_length=255)  # Giờ làm việc, ví dụ: "9:00 AM - 6:00 PM"
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=255)  # Tên môn học
    code = models.CharField(max_length=20)  # Mã môn học
    instructor = models.CharField(max_length=255)  # Giảng viên

    def __str__(self):
        return self.name

class TimeTable(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)  # Ngày trong tuần (Thứ 2, Thứ 3, ...)
    start_time = models.TimeField()  # Thời gian bắt đầu
    end_time = models.TimeField()  # Thời gian kết thúc
    room = models.CharField(max_length=50)  # Phòng học

    def __str__(self):
        return f'{self.course.name} - {self.day_of_week} {self.start_time}-{self.end_time}'
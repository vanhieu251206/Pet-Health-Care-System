from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)  # ID nhân viên (tự động tăng)
    name = models.CharField(max_length=100)  # Tên nhân viên
    age = models.IntegerField()  # Tuổi
    email = models.EmailField()  # Email (định dạng email)


    def __str__(self):
        return f"{self.employee_id} - {self.name}"

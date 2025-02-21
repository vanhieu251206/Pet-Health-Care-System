from django.db import models

class Room(models.Model):
    STATUS_CHOICES = [
        ('available', 'Trống'),
        ('booked', 'Đã có thú cưng'),
    ]
    room_code = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    pet_name = models.CharField(max_length=50, blank=True, null=True)
    owner_name = models.CharField(max_length=50, blank=True, null=True)
    check_in_date = models.DateField(blank=True, null=True)
    expected_check_out_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.room_code
    

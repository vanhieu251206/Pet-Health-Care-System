from django.db import models


class PhongLuuTru(models.Model):
    MA_LOAI_CHUONG = [
        ('Nhỏ', 'Nhỏ'),
        ('Trung Bình', 'Trung bình'),
        ('Lớn', 'Lớn'),
    ]

    TRANG_THAI_PHONG = [
        ('Trống', 'Trống'),
        ('Có Thú Cưng', 'Đã có thú cưng'),
    ]

    ma_phong = models.CharField(max_length=10, unique=True, verbose_name="Mã phòng")
    trang_thai = models.CharField(max_length=20, choices=TRANG_THAI_PHONG, default='Trống', verbose_name="Trạng thái")
    loai_chuong = models.CharField(max_length=20, choices=MA_LOAI_CHUONG, verbose_name="Loại chuồng")
    ten_thu_cung = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tên thú cưng")
    ngay_nhan = models.DateField(blank=True, null=True, verbose_name="Ngày nhận")
    ngay_tra_du_kien = models.DateField(blank=True, null=True, verbose_name="Ngày trả dự kiến")

    def __str__(self):
        return f"{self.ma_phong} - {self.get_trang_thai_display()}"
class Booking(models.Model):
    TRANG_THAI_CHOICES = [
        ('cho_xac_nhan', 'Chờ xác nhận'),
        ('da_xac_nhan', 'Đã xác nhận'),
        ('huy', 'Đã hủy'),
    ]

    ma_booking = models.CharField(max_length=20, unique=True, verbose_name="Mã Booking")
    ten_khach_hang = models.CharField(max_length=255, verbose_name="Tên khách hàng")
    ten_thu_cung = models.CharField(max_length=255, verbose_name="Tên thú cưng")
    check_in = models.DateField(verbose_name="Ngày Check-in")
    check_out = models.DateField(verbose_name="Ngày Check-out")
    trang_thai = models.CharField(max_length=20, choices=TRANG_THAI_CHOICES, default='cho_xac_nhan', verbose_name="Trạng thái")
    thanh_toan = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Thanh toán (VNĐ)")

    def __str__(self):
        return f"{self.ma_booking} - {self.ten_khach_hang}"

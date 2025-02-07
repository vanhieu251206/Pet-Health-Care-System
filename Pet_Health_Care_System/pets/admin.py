from django.contrib import admin
from .models import Product

# Đăng ký model Pet với admin
admin.site.register(Product)
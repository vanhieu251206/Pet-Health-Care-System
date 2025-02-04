from django.contrib import admin
from .models import Pet

# Đăng ký model Pet với admin
admin.site.register(Pet)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, CustomUser

# Đăng ký model Pet với admin
admin.site.register(Product)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'phone', 'role', 'is_staff', 'is_active', 'date_joined')
    
    list_filter = ('is_staff', 'is_active', 'role')
    
    search_fields = ('username', 'email', 'phone')
    
    ordering = ('date_joined',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Thông tin cá nhân', {'fields': ('first_name', 'last_name', 'email', 'phone', 'avatar', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'phone', 'avatar', 'role', 'is_staff', 'is_active'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

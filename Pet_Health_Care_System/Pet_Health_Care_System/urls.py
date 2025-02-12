from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pets/', include('pets.urls')),    # Trỏ đến ứng dụng pets
    path('staff/', include('staff.urls')),  # Trỏ đến ứng dụng staff
    path('doctor/', include('doctor.urls')),  # Trỏ đến ứng dụng doctor
    path('', include('QTV.urls')),  # Trỏ đến ứng dụng QTV (Trang chủ hoặc Dashboard)
]

# Xử lý media nếu đang ở chế độ DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

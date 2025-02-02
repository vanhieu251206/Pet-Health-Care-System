from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializer cho model User
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSet cho model User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Router của Django REST Framework
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)  # URL: /router/users/

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),                # URL: /admin/
    path('pets', include('pets.urls')),           # URL: /pets/
    path('api/', include(router.urls)),            # URL: /api/users/ (thay vì /router/users/)
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # URL: /api-auth/
    path('', include('staff.urls')),               # URL mặc định ("/") trỏ đến staff.urls
]

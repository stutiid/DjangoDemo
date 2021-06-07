from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from tutorial.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

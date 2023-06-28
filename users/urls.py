from django.urls import path, include
from .views import UserViewSet, UserValidation
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('validate/', UserValidation.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

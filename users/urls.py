from django.urls import path, include
from .views import UserViewSet, UserValidation
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('validate/', UserValidation.as_view())
]

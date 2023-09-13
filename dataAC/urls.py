from django.urls import path, include
from .views import DataViewSet
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'dataAC', DataViewSet)

urlpatterns = [
    path('', include(router.urls))
]
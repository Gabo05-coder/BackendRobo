from django.urls import path, include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

postsRouter = DefaultRouter()
postsRouter.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(postsRouter.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

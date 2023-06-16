from django.urls import path, include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

postsRouter = DefaultRouter()
postsRouter.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(postsRouter.urls))
]

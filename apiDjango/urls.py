from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
#from users import urls

urlpatterns = [
    path('api/', include('users.urls')),
    path('api/', include('posts.urls')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from rest_framework import viewsets
from .models import Posts
from .serializer import postSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = postSerializer

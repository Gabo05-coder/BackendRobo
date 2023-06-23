from rest_framework import serializers
from .models import Posts

class postSerializer(serializers.ModelSerializer):
    class Meta():
        model = Posts
        fields = ('__all__')
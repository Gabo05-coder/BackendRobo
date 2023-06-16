from rest_framework import serializers
from .models import Posts

class postSerializer(serializers.ModelSerializer):
    class Meta():
        model = Posts
        fields = ('__all__')

"""
class likesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Likes
        fields = ('__all__')

class participantsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Participants
        fields = ('__all__')
"""
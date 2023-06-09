from rest_framework import serializers
from .models import Posts, Likes, Participants

class postSerializer(serializers.ModelSerializer):
    model = Posts
    class meta():
        fields = ('__all__')

class likesSerializer(serializers.ModelSerializer):
    model = Likes
    class meta():
        fields = ('__all__')

class participantsSerializer(serializers.ModelSerializer):
    model = Participants
    class meta():
        fields = ('__all__')
from rest_framework import serializers
from .models import Posts, Likes, Participants

class postSerializer(serializers.ModelSerializer):
    model = Posts
    class meta():
        fields = ('author', 'description', 'createdDate', 'date')

class likesSerializer(serializers.ModelSerializer):
    model = Likes
    class meta():
        fields = ('likedPost','likerUser')

class participantsSerializer(serializers.ModelSerializer):
    model = Participants
    class meta():
        fields = ('participatedPost','participatingUser')
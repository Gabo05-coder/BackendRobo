from rest_framework import serializers
from .models import User

class userSerializer(serializers.ModelSerializer):
    model = User
    class meta:
        fields = ('username','email', 'password')

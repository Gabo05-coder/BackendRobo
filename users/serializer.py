from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('__all__')

class UserValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password')

from rest_framework import serializers
from .models import dataAC

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = dataAC
        fields = ('__all__')

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer, UserValidationSerializer

from rest_framework import viewsets
from .models import Users

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

"""class UserValidation(APIView):
    def post(self, request):
        data = request.data

        try:
            queryset = Users.objects.filter(username = data['username'], password = data['password'])
            print(queryset)
        except Users.DoesNotExist:
            return Response({'error' : 'The data does not exist in the database'})
        
        serializer = UserSerializer(queryset)
        return Response(serializer.data, status=200)
        """

class UserValidation(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserValidationSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            results = Users.objects.filter(username=username, password=password)
            
            resultados_serializados = UserValidationSerializer(results, many=True)
            return Response(resultados_serializados.data)
        
        return Response({'error' : 'The data does not exist in the database'})






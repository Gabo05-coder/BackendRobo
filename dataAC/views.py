from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import dataAC
from .serializer import DataSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = dataAC.objects.all()
    serializer_class = DataSerializer

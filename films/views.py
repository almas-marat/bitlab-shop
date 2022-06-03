from django.shortcuts import render
from rest_framework import viewsets
from .models import Films
from .serializers import FilmsSerializer

class FilmsViewSet(viewsets.ModelViewSet):
    serializer_class = FilmsSerializer
    queryset = Films.objects.all()

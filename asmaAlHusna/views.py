from django.shortcuts import render
from .serializers import AsmaalhusnaSerializer
from rest_framework import generics, viewsets
from .models import AsmaAlHusna

# Create your views here.

class AsmaalhusnaList(generics.ListAPIView):
    queryset = AsmaAlHusna.objects.all()
    serializer_class = AsmaalhusnaSerializer

class AsmaalhusnaDetail(generics.RetrieveAPIView):
    queryset = AsmaAlHusna.objects.all()
    serializer_class = AsmaalhusnaSerializer
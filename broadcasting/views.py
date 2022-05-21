from django.shortcuts import render
from yaml import serialize
from .models import Broadcasting
from .serializers import BroadcastingSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class BroadcastingListAPIView(generics.ListAPIView):
    queryset = Broadcasting.objects.all()
    serializer_class = BroadcastingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status_type']

class BroadcastingRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Broadcasting.objects.all()
    serializer_class = BroadcastingSerializer
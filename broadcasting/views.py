from django.shortcuts import render
from yaml import serialize
from .models import Broadcasting
from .serializers import BroadcastingSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

class BroadcastingListAPIView(generics.ListAPIView):
    queryset = Broadcasting.objects.all()
    serializer_class = BroadcastingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status_type']
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title_ar', 'title_en', 'riwaya_en', 'riwaya_ar']

class BroadcastingRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Broadcasting.objects.all()
    serializer_class = BroadcastingSerializer
from django.shortcuts import render
from .models import Category, Container, Component
from .serializers import CategorySerializer, ComponentSerializer, ContainerSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContainerList(generics.ListAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class ContainerDetail(generics.RetrieveAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer

class ComponentList(generics.ListAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['container']


class ComponentDetail(generics.RetrieveAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

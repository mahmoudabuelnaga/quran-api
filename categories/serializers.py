from dataclasses import field
from rest_framework import serializers
from .models import Category, Container, Component


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ['id', 'container', 'bismillah', 'body', 'surat', 'looper']

class ContainerSerializer(serializers.ModelSerializer):
    components = ComponentSerializer(many=True)

    class Meta:
        model = Container
        fields = ['id', 'title', 'title_ar', 'slug', 'category', 'components']

class CategorySerializer(serializers.ModelSerializer):
    containers = ContainerSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'title_ar', 'slug', 'containers']

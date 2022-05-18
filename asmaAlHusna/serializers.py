from re import A
from rest_framework import serializers
from .models import AsmaAlHusna

class AsmaalhusnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsmaAlHusna
        fields = ['id', 'number','name', 'transliteration', 'meaning']
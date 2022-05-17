from rest_framework import serializers
from .models import Reader, Recitations

# Create your serializers here.

class RecitationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recitations
        fields = ['id', 'reader', 'number', 'name', 'download_surat_link', 'surat_time']


class ReaderSerializer(serializers.ModelSerializer):
    recitations = RecitationsSerializer(many=True)

    
    class Meta:
        model = Reader
        fields = ['id','name', 'recitations']
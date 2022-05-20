from rest_framework import serializers
from .models import Broadcasting

class BroadcastingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broadcasting
        fields = ['id', 'title_en', 'title_ar', 'riwaya_en', 'riwaya_ar', 'broadcasting', 'status_type']
        
from rest_framework import serializers
from .models import VisitorImage

class VisitorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorImage
        fields = ('id', 'image', 'face_detected', 'visitor')
from django.shortcuts import render



# Create your views here.
import face_recognition
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import VisitorImage
from .serializers import VisitorImageSerializer
from rest_framework.viewsets import ModelViewSet


class FaceRecognitionView(ModelViewSet):
    queryset = VisitorImage.objects.all()
    serializer_class = VisitorImageSerializer
    
    
    
    def post(self, request):
        image_file = request.FILES.get('image')
        if not image_file:
            return Response({'error': 'No image provided'}, status=400)

        # Load the image
        image = face_recognition.load_image_file(image_file)

        # Detect faces in the image
        face_locations = face_recognition.face_locations(image)

        # Check if at least one face is detected
        face_detected = len(face_locations) > 0

        # Save the image and face detection result
        visitor_image = VisitorImage.objects.create(
            image=image_file,
            face_detected=face_detected,
            # Add other fields as needed
        )

        return Response({'face_detected': face_detected})
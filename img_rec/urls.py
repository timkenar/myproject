from django.urls import path
from .views import FaceRecognitionView

urlpatterns = [
    path('face-recognition/', FaceRecognitionView.as_view({'post': 'post'}), name='face_recognition'),
]
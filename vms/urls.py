from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from main.views import VisitorViewSet, HostViewSet, AppointmentViewSet
from img_rec.views import FaceRecognitionView



router = DefaultRouter()
router.register(r'visitors', VisitorViewSet)
router.register(r'hosts', HostViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'face-recognition', FaceRecognitionView, basename='face-recognition')



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('img_rec.urls')),
    #path('', include('main.urls'))


] 

urlpatterns

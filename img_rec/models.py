from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Visitor(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, default='')
    photo = models.ImageField(upload_to='visitor_photos/')

    def __str__(self):
        return self.name.username

class VisitorImage(models.Model):
    image = models.ImageField(upload_to='visitor_images/')
    face_detected = models.BooleanField(default=False)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, related_name='images')
    # Add any other relevant fields

    def __str__(self):
        return f'Image for {self.visitor}'
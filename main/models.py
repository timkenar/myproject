from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Host(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Visitor(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, default='')
    photo = models.ImageField(upload_to='visitor_photos/')

    def __str__(self):
        return self.name.username

class Appointment(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    date = models.DateTimeField()
    purpose = models.TextField()

    def __str__(self):
        return f"{self.visitor.name.username} with {self.host.name} on {self.date}"

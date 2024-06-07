from rest_framework import serializers
from .models import Visitor, Host, Appointment

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['name', 'email','photo']

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['name','email','name']

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['visitor', 'host', 'date', 'purpose']

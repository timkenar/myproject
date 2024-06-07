from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Visitor, Host, Appointment
from .serializers import VisitorSerializer, HostSerializer, AppointmentSerializer

class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    permission_classes = [IsAuthenticated]

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    permission_classes = [IsAuthenticated]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        appointment = serializer.save()
        # Generate a receipt after saving
        self.generate_receipt(appointment)

    def generate_receipt(self, appointment):
        # Add your receipt generation logic here
        print(f"Receipt: {appointment.visitor.name.username} -> {appointment.host.name} on {appointment.date}")


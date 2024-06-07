from django.contrib import admin
from .models import Host, Visitor, Appointment

# Register your models here.


admin.site.register(Host)
admin.site.register(Visitor)
admin.site.register(Appointment)

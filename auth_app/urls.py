from django.urls import path
from .views import RegisterVisitorView, RegisterHostView, LoginView

urlpatterns = [
    path('register/visitor/', RegisterVisitorView.as_view(), name='register_visitor'),
    path('register/host/', RegisterHostView.as_view(), name='register_host'),
    path('login/', LoginView.as_view(), name='login'),
]

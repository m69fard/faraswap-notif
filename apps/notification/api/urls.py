from django.urls import path

from .views import OTPAPIView

urlpatterns = [
    path("otp", OTPAPIView.as_view()),
]



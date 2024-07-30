from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.notification.utils import send_otp
from services.authentication import get_phone_number


class OTPAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        token = request.auth
        phone_number = get_phone_number(token)
        if not phone_number:
            return Response({"error": "User does not have a phone number or invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        send_otp(phone_number)
        return Response({"message": "OTP is being sent"}, status=status.HTTP_200_OK)
from datetime import timedelta
from unittest.mock import patch

import jwt
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

SIGNING_KEY = settings.SIGNING_KEY


class TestNotification(APITestCase):

    def setUp(self):
        self.user_id = 1
        self.phone_number = "09121001010"

        self.token = jwt.encode(
            {
                "token_type": "access",
                "user_id": self.user_id,
                "exp": timezone.now() + timedelta(hours=1),
                "iat": timezone.now(),
                "jti": "d26217daee5b48bfba233036e5d64888",
            },
            SIGNING_KEY,
            algorithm="HS256",
        )

    @patch("apps.notification.api.views.get_phone_number")
    @patch("apps.notification.utils.send_sms.delay")
    def test_request_otp(self, mock_send_sms_delay, mock_get_phone_number):

        mock_get_phone_number.return_value = self.phone_number

        url = reverse("otp")
        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.client.post(
            url,
            headers=headers,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

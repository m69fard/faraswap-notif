import requests
from django.conf import settings


def get_phone_number(token):
    url = f"{settings.AUTH_SERVICE_URL}/api/v1/auth/user"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('phone_number')
    return None
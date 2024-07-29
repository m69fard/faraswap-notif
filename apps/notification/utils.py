import random

from .tasks import send_sms


def send_otp(phone_number):
    otp = random.randint(100000, 999999)
    send_sms.delay(phone_number, otp)
    print(f"Sending OTP {otp} to {phone_number}")
    return otp
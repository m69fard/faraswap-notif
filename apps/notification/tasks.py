import random

from celery import shared_task


def send_otp(phone_number):
    otp = random.randint(100000, 999999)
    send_sms(phone_number, otp)
    print(f"Sending OTP {otp} to {phone_number}")
    return otp

@shared_task
def send_sms(phone_number, message):
    # Placeholder function to simulate sending an SMS
    print(f"Sending message: {message} to phone number: {phone_number}")
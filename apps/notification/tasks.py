from celery import shared_task


@shared_task
def send_sms(phone_number, message):
    # Placeholder function to simulate sending an SMS
    print(f"Sending message: {message} to phone number: {phone_number}")
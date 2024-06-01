import smtplib

from celery import shared_task
from django.core.mail import send_mail

from config import settings
from materials.models import Course


@shared_task
def send_email_update(pk, user_id, user_email):
    instance = Course.objects.get(pk=pk)
    subscribe = instance.subscription_set.all().filter(user=user_id)
    email_list = [user_email for subscribe.user in subscribe]
    message_subject = f'Обновление курса {instance}'
    message_text = f'Курс {instance} обновлён. Добавили много нового'
    try:
        server_response = send_mail(
            subject=message_subject,
            message=message_text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=email_list,
            fail_silently=False,
        )
    except smtplib.SMTPException as e:
        server_response = e
    return server_response

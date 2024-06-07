from datetime import datetime, timedelta

import pytz

from config import settings
from users.models import User


def check_last_login():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    users = User.objects.all().filter(is_active=True)
    for user in users:
        if current_datetime - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()

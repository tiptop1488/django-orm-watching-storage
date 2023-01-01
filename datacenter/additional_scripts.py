import time
from django.utils import timezone


def get_duration(user):
    time_entered = user.entered_at
    leaved_at = user.leaved_at
    if leaved_at:
        delta = leaved_at - time_entered
        delta = delta.seconds
    else:
        now = timezone.now()
        delta = now - time_entered
        delta = delta.total_seconds()
    return delta


def format_duration(delta):
    time_in_storage = time.strftime("%H:%M:%S", time.gmtime(delta))
    return time_in_storage


def is_visit_long(delta):
    hour = 3600
    if delta > hour:
        return True
    else:
        return False
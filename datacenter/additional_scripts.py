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
    hours = delta // 3600
    minutes = (delta % 3600) // 60
    time_in_storage = f'{hours:02}ч {minutes:02}мин'
    return time_in_storage


def is_visit_long(delta):
    hour = 3600
    return delta > hour

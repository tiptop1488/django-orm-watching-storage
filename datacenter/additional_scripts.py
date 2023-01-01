from django.utils import timezone


def get_duration(visit):
    time_entered = visit.entered_at
    leaved_at = visit.leaved_at
    if leaved_at:
        delta = leaved_at - time_entered
        delta = delta.seconds
    else:
        now = timezone.now()
        delta = now - time_entered
        delta = delta.total_seconds()
    return delta


def format_duration(duration):
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    time_in_storage = f'{int(hours):02}ч {int(minutes):02}мин'
    return time_in_storage


def is_visit_long(duration):
    hour = 3600
    return duration > hour

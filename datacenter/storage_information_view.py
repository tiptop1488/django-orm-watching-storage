from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
import time


def get_duration(user):
    time_entered = user.entered_at
    leaved_at = user.leaved_at
    if leaved_at:
        delta = leaved_at - time_entered
        delta = delta.seconds
    else:
        now = timezone.now()
        delta = now - time_entered
        delta = delta.seconds
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


def storage_information_view(request):
    non_closed_visits = []

    users_in_storage = Visit.objects.filter(leaved_at=None)

    for user in users_in_storage:

        delta = get_duration(user)
        duration = format_duration(delta)
        is_strange = is_visit_long(delta)

        user_info = {
        'who_entered': user.passcard.owner_name,
        'entered_at': user.entered_at,
        'duration': duration,
        'is_strange': is_strange,
        }

        non_closed_visits.append(user_info)

    context = {
        'non_closed_visits': non_closed_visits,
    }

    return render(request, 'storage_information.html', context)

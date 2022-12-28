from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import time
from django.utils import timezone
from django.shortcuts import get_object_or_404


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


def passcard_info_view(request, passcode):

    passcard = Passcard.objects.all()[0]
    user = get_object_or_404(Passcard, passcode=passcode)
    all_visits = Visit.objects.filter(passcard=user)
    this_passcard_visits = []

    for visit in all_visits:
        delta_visit = get_duration(visit)
        time_visit = format_duration(delta_visit)
        is_strange = is_visit_long(delta_visit)
        visit_info = {
            'entered_at': visit.entered_at,
            'duration': time_visit,
            'is_strange': is_strange,
        }
        this_passcard_visits.append(visit_info)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)

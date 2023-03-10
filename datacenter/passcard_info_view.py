from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import additional_scripts


def passcard_info_view(request, passcode):
    user = get_object_or_404(Passcard, passcode=passcode)
    all_passcards = Visit.objects.filter(passcard=user)
    this_passcard_visits = []

    for visit in all_passcards:
        delta_visit = additional_scripts.get_duration(visit)
        time_visit = additional_scripts.format_duration(delta_visit)
        is_strange = additional_scripts.is_visit_long(delta_visit)
        visit_info = {
            'entered_at': visit.entered_at,
            'duration': time_visit,
            'is_strange': is_strange,
        }
        this_passcard_visits.append(visit_info)

    context = {
        'passcard': user,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)

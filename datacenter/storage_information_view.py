from datacenter.models import Visit
from django.shortcuts import render
from . import additional_scripts


def storage_information_view(request):
    non_closed_visits = []

    users_in_storage = Visit.objects.filter(leaved_at=None)

    for user in users_in_storage:

        delta = additional_scripts.get_duration(user)
        duration = additional_scripts.format_duration(delta)
        is_strange = additional_scripts.is_visit_long(delta)

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

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def passcard_info_view(request, passcode):
    this_passcard_visits = [
    ]
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        enter = timezone.localtime(visit.entered_at)
        duration = visit.format_duration()
        is_strange = visit.is_strange()
        this_passcard_visits.append(
            {
                'entered_at': enter,
                'duration': duration,
                'is_strange': is_strange
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

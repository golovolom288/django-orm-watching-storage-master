from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


from django.db import models

import datetime


def passcard_info_view(request, passcode):
    this_passcard_visits = [
    ]
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    now = timezone.localtime()
    for visit in visits:
        enter = timezone.localtime(visit.entered_at)
        if visit.leaved_at is None:
            enter = timezone.localtime(visit.entered_at)
            delta = now - enter
            if delta.total_seconds() / 60 < 60:
                this_passcard_visits.append(
                    {
                        'entered_at': enter,
                        'duration': delta,
                        'is_strange': False
                    }
                )
            else:
                this_passcard_visits.append(
                    {
                        'entered_at': enter,
                        'duration': delta,
                        'is_strange': True
                    }
                )
        else:
            leave = timezone.localtime(visit.leaved_at)
            delta = leave - enter
            if delta.total_seconds() / 60 < 60:
                this_passcard_visits.append(
                    {
                        'entered_at': enter,
                        'duration': delta,
                        'is_strange': False
                    }
                )
            else:
                this_passcard_visits.append(
                    {
                        'entered_at': enter,
                        'duration': delta,
                        'is_strange': True
                    }
                )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

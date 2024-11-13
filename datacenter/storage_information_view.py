from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.all.leaved_at()
    now = timezone.localtime()
    for visit in visits:
        enter = timezone.localtime(visit.entered_at)
        duration = now - enter
        non_closed_visits.append(
            {
                'who_entered': visit.passcard,
                'entered_at': enter,
                'duration': duration,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):

    non_closed_visits = []
    passcards = Visit.objects.all()
    now = timezone.localtime()
    count = 0
    for passcard in passcards:
        if passcard.leaved_at is None:
            then = timezone.localtime(passcard.entered_at)
            duration = now - then
            non_closed_visits.append(
                {
                    'who_entered': passcard.passcard,
                    'entered_at': then,
                    'duration': duration,
                }
            )
            count += 1
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

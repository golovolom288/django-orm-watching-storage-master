from django.utils import timezone

from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)
    seconds_per_hour = 3600
    seconds_per_minute = 60

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        enter = timezone.localtime(self.entered_at)
        if self.leaved_at:
            leave = timezone.localtime(self.leaved_at)
            return (leave - enter).total_seconds()
        else:
            now = timezone.localtime()
            return (now - enter).total_seconds()

    def is_strange(self):
        return self.get_duration() > self.seconds_per_hour

    def format_duration(self):
        duration = self.get_duration()
        hours = int(duration // self.seconds_per_hour)
        minutes = int((duration % self.seconds_per_hour) // self.seconds_per_minute)
        print(duration)
        return f"{hours} ч. {minutes} мин."




from django.db import models
from django.core.exceptions import ValidationError

from datetime import date


class Reservation(models.Model):
    FIRST_TIME = '7-8'
    SECOND_TIME = '8-9'
    THIRD_TIME = '9-10'
    FORTH_TIME = '10-11'
    FIFTH_TIME = '11-12'
    SIXTH_TIME = '14-15'
    LAST_TIME = '15-16'
    RESERVATION_TIMES = [
        (FIRST_TIME, FIRST_TIME),
        (SECOND_TIME, SECOND_TIME),
        (THIRD_TIME, THIRD_TIME),
        (FORTH_TIME, FORTH_TIME),
        (FIFTH_TIME, FIFTH_TIME),
        (SIXTH_TIME, SIXTH_TIME),
        (LAST_TIME, LAST_TIME)
    ]

    full_name = models.CharField()
    nationality_id = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    date = models.DateField()
    time = models.CharField(max_length=6, choices=RESERVATION_TIMES, default=FIRST_TIME)
    datetime_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [
            ['nationality_id', 'phone_number'],
            ['date', 'time']
        ]

    def __str__(self):
        return f'{self.nationality_id} - {self.full_name}'
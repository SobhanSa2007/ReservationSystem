from django.core.management.base import BaseCommand

from  datetime import date
import pytz

from reservation.models import Reservation


class Command(BaseCommand):
    help = 'Remove all expired Reservation'

    def handle(self, *args, **options):
        today = date.today()
        expired_reservations = Reservation.objects.filter(date__lt=today)

        count = expired_reservations.count()
        expired_reservations.delete()

        self.stdout.write(self.style.SUCCESS(f'{count} expired reservations deleted'))
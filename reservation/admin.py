from django.contrib import admin

from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'nationality_id',
        'full_name', 'phone_number',
        'datetime_created'
    ]
    search_fields = [
        'nationality_id',
        'phone_number',
        'full_name'
    ]
    list_filter = ['datetime_created']
    list_per_page = 30
    ordering = ['id']

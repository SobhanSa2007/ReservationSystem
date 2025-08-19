from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

import calendar
from datetime import date

from .forms import MakeReservationForm
from .models import Reservation


class ReservationListView(View):
    """
        getting month and its days
        -to show them in the template
        -by a calendar.
    """

    template_name = 'reservation/reservation_list.html'

    def get(self, request):
        today = date.today()
        year = today.year
        month = today.month
        today_day = today.day

        # the count of days in current month
        days_in_month = calendar.monthrange(year=year, month=month)[1]

        # list of days (1 to 30/31)
        days = list(range(1, days_in_month + 1))

        month_name = calendar.month_name[month]

        return render(
            request,
            template_name=self.template_name,
            context={
                'year': year,
                'month': month,
                'month_name': month_name,
                'days': days,
                'today_day': today_day
            }
        )
    

class MakeReservationView(View):
    template_name = 'reservation/make_reservation.html'
    form = MakeReservationForm

    def get(self, request, year, month, day):
        reservation_date = date(year=year, month=month, day=day)
        form = self.form(reservation_date=reservation_date)
        return render(
            request, template_name=self.template_name,
            context={
                'form':form,
                'reservation_date':reservation_date
            }
        )

    def post(self, request, year, month, day):
        reservated_date = date(year=year, month=month, day=day)
        form = self.form(request.POST, reservation_date=reservated_date)
        if form.is_valid():
            cd = form.cleaned_data

            # reservation = Reservation.objects.filter(
            #     date=reservated_date,
            #     time=cd['time']
            # )
            # if reservation:
            #     messages.error(request, 'there is a reservation at this time', 'danger')
            #     return redirect('reservation:reservation_list')

            user_reservations = request.session.get('user_reservations', [])
            new_reservation = {
                'full_name':cd['full_name'],
                'nationality_id':cd['nationality_id'],
                'phone_number':cd['phone_number'],
                'date':str(reservated_date),
                'time':cd['time']
            }
            user_reservations.append(new_reservation)
            request.session['user_reservations']=user_reservations

            Reservation.objects.create(
                full_name=cd['full_name'],
                nationality_id=cd['nationality_id'],
                phone_number=cd['phone_number'],
                date=reservated_date,
                time=cd['time']
            )

            messages.success(
                request,
                f'You have made a reservation. Date:{reservated_date} - Time:{cd['time']}',
                'success'
            )
            return redirect('reservation:user_reservation')
        return render(request, template_name=self.template_name, context={
            'form':form,
            'reservation_date':reservated_date
        })
    

class UserReservationView(View):
    template_name = 'reservation/user_reservation.html'

    def get(self, request):
        user_reservations = request.session.get('user_reservations', [])
        if user_reservations:
            return render(
                request,
                template_name=self.template_name,
                context={'user_reservations':user_reservations}
            )
            
        messages.warning(
            request,
            'Sorry There is no reservation for you Or your reservation may not have been created.',
            'warning'
        )
        return render(request, template_name=self.template_name)
    

class ReservationDeleteView(View):
    template_name = 'reservation/reservation_delete.html'

    def get(self, request, natid):
        return render(request, template_name=self.template_name, context={'natid':natid})
    

class ReservationDeleteDoneView(View):
    def post(self, request, natid):
        reservation = get_object_or_404(Reservation, nationality_id=natid)
        reservation.delete()
        user_reservations = request.session.get('user_reservations', [])
        user_reservations = [
            i for i in user_reservations if i.get('nationality_id') != natid
        ]
        request.session['user_reservations'] = user_reservations
        messages.success(request, 'The reservation deleted successfully.', 'success')
        return redirect('reservation:user_reservation')
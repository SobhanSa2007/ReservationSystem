from django import forms

from .models import Reservation


class MakeReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'full_name',
            'nationality_id',
            'phone_number',
            'time',
        ]

    def __init__(self, *args, **kwargs):
        self.reservation_date = kwargs.pop('reservation_date', None)
        super().__init__(*args, **kwargs)

    def clean_nationality_id(self):
        user_nat_id = self.cleaned_data['nationality_id']
        if Reservation.objects.filter(nationality_id=user_nat_id).exists():
            raise forms.ValidationError(f'This NatID {user_nat_id} is allready exists!')
        return user_nat_id
    
    def clean_phone_number(self):
        user_phone_number = self.cleaned_data['phone_number']
        if Reservation.objects.filter(phone_number=user_phone_number).exists():
            raise forms.ValidationError(f'This PhoneNumber {user_phone_number} is allready exists!')
        return user_phone_number
    
    def clean_time(self):
        time = self.cleaned_data.get('time')
        if self.reservation_date and time:
            exists = Reservation.objects.filter(
                date=self.reservation_date,
                time=time
            ).exists()

            if exists:
                raise forms.ValidationError('There is a reservation at this time')
        return time
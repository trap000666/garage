# garage/forms.py

from django import forms
from .models import Booking, SERVICE_CHOICES, STATUS_CHOICES
import datetime


class BookingForm(forms.ModelForm):
    preferred_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': str(datetime.date.today())}),
        label="Preferred Date"
    )
    preferred_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label="Preferred Time"
    )

    class Meta:
        model = Booking
        fields = [
            'customer_name', 'customer_phone', 'customer_email',
            'vehicle_make', 'vehicle_model', 'vehicle_year', 'number_plate',
            'service_type', 'description',
            'preferred_date', 'preferred_time',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class BookingStatusForm(forms.ModelForm):
    """Form for garage staff to update booking status and add notes."""
    class Meta:
        model = Booking
        fields = ['status', 'mechanic_notes']
        widgets = {
            'mechanic_notes': forms.Textarea(attrs={'rows': 4}),
        }
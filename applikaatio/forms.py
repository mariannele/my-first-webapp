from django import forms
from .models import Businesstrip

class BusinesstripForm(forms.ModelForm):
    class Meta:
        model = Businesstrip
        fields = ['travel_date', 'departure', 'destination', #'roundtrip',
        'reason', 'company', 'total_km', 'km_allowance_eur', 'notes', #'compensation_applied'
        ]
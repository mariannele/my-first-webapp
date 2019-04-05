from django import forms
from django.forms import ModelForm, TextInput
from .models import Businesstrip, Traveldestination

class BusinesstripForm(forms.ModelForm):
    class Meta:
        model = Businesstrip
        fields = ['travel_date', 'departure', 'destination', #'roundtrip',
        'reason', 'company', 'total_km', 'km_allowance_eur', #'notes', #'compensation_applied'
        ]

class CityForm(ModelForm):
    class Meta:
        model = Traveldestination
        fields = ['city_name']
        widgets = {
            'city_name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder
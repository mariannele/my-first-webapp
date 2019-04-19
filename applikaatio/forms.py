from django import forms
from django.forms import ModelForm, TextInput
from .models import Businesstrip

class BusinesstripForm(forms.ModelForm):
    class Meta:
        model = Businesstrip
        fields = ['date_posted', 'travel_date', 'title', 'city_name', 'trip_type',
        'content', 'accommodation']

"""class CityForm(ModelForm):
    class Meta:
        model = Businesstrip
        fields = ['city_name']
        widgets = {
            'city_name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        }"""
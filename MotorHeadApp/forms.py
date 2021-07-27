from django import forms
import datetime
from .models import Stats


class DateInput(forms.DateInput):
    input_type = 'date'


class StatsForm(forms.ModelForm):
    class Meta:
        model = Stats
        exclude = ['user']
        widgets = {
            'date': DateInput()
        }

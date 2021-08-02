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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'date'):
            self.initial['date'] = datetime.datetime.now()

from django import forms
import datetime
from django.forms.models import ModelChoiceField
from .models import Stats
from django.contrib.auth.models import User


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


class UpdateStatsForm(forms.ModelForm):
    class Meta:
        model = Stats
        exclude = ['user']
        widgets = {
            'date': DateInput()
        }


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.first_name + ' ' + obj.last_name


class SearchByMotor(forms.Form):
    start_date = forms.CharField(label='Start Date', max_length=12, widget=DateInput())
    end_date = forms.CharField(label='End Date', max_length=12, widget=DateInput(), initial=datetime.date.today)
    motor = MyModelChoiceField(queryset=User.objects.filter(groups__name='motorhead_users'))

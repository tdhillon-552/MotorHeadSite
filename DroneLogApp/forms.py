from django import forms
import datetime
from django.forms.models import ModelChoiceField
from .models import MissionTable



class DateInput(forms.DateInput):
    input_type = 'date'


class MissionForm(forms.ModelForm):
    class Meta:
        model = MissionTable
        exclude = ['user']
        widgets = {
            'date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and hasattr(self.instance, 'date'):
            self.initial['date'] = datetime.datetime.now()


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.first_name + ' ' + obj.last_name




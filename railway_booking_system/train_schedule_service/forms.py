# forms.py

from django import forms
from .models import Train, TrainSchedule

class TrainForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrainForm, self).__init__(*args, **kwargs)
        first_way = [("COLOMBO - JAFFNA", "COLOMBO - JAFFNA"),
                     ("COLOMBO - GALLE", "COLOMBO - GALLE"),
                     ("COLOMBO - BADULLA", "COLOMBO - BADULLA"),
                     ("COLOMBO - TRINCOMALE", "COLOMBO - TRINCOMALE")]
        self.fields['route'].widget = forms.Select(choices=first_way)

    class Meta:
        model = Train
        fields = ['train_name', 'route']

class TrainScheduleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrainScheduleForm, self).__init__(*args, **kwargs)
        locations = [("COLOMBO", "COLOMBO"),
                     ("JAFFNA", "JAFFNA"),
                     ("GALLE", "GALLE"),
                     ("BADULLA", "BADULLA"),
                     ("TRINCOMALE", "TRINCOMALE")]
        self.fields['start_location'].widget = forms.Select(choices=locations)
        self.fields['destination'].widget = forms.Select(choices=locations)

        departure_times = [('{}:00'.format(hour), '{}:00'.format(hour)) for hour in range(8, 24)] + [('00:00', '00:00')]
        self.fields['departure_time'].widget = forms.Select(choices=departure_times)

    class Meta:
        model = TrainSchedule
        fields = ['train', 'schedule_date', 'departure_time','start_location', 'destination']


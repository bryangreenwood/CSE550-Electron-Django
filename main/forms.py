from django import forms

class Chartinput(forms.Form): 
    start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    Local_Timezone = forms.BooleanField(required=False)
 
    # def __init__(self, *args, **kwargs):
    #     super(Chartinput, self).__init__(*args, **kwargs)
    #     self.initial['start'] = '2020-01-18'
    #     self.initial['end'] = '2020-01-19'
    #     self.initial['device'] = '310'
    #     self.initial['Local_Timezone'] = False

class Devicechoice(forms.Form):
    DEVICE_CHOICES = (
        ('310', '310'),
        ('311', '311'),
        ('312', '312')
    )
    device = forms.ChoiceField(choices=DEVICE_CHOICES)

class Yaxischoice(forms.Form):
    choices = (
        ('Acc_magnitude_avg', 'Average Acceleration'),
        ('eda_avg', 'Average EDA'),
        ('Temp_avg', 'Average Temperature'),
        ('movement_intensity', 'Movement Intensity'),
        ('Steps', 'Steps'),
        ('rest', 'Rest'),
        ('on_wrist', 'On Wrist')
    )

    y_axis = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label='Variables to import and display', choices=choices)

from django import forms

class Chartinput(forms.Form):
    start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    device = forms.CharField(max_length=200)
    utc = forms.BooleanField(required=False)
from django.shortcuts import render
from django.http import HttpResponse
from main.models import Sensor, Sensordata
import plotly.express as px
from .forms import Chartinput
# Create your views here.

def main_page(request):
    data = Sensordata.objects.filter(sensor__sensor_number='310', UTC_Datetime__range=['2020-01-18', '2020-01-19']).order_by('UTC_Datetime')

    fig = px.line(
        x=[xvar.UTC_Datetime for xvar in data],
        y=[yvar.Acc_magnitude_avg for yvar in data],
        title='Magnitude of Acceleration Average over time',
        labels={'x':'Time', 'y':'Magnitude of Acceleration Average'}
    )
    fig.update_layout(title={
        'font_size' : 20,
        'xanchor' : 'center',
        'x': 0.5,
    })

    chart = fig.to_html()
    context = {'chart': chart, 'form': Chartinput()}
    return render(request, 'main/main_page.html', context)
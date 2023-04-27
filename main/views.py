from django.shortcuts import render
from django.http import HttpResponse
from main.models import Sensordata
import plotly.express as px
from .forms import Chartinput , Devicechoice, Yaxischoice
from datetime import timedelta, datetime
import pandas
from Group5.utils import style_df
from plotly.subplots import make_subplots
import plotly.graph_objects as go
# Create your views here.

def main_page(request):
    # Set default variables for forms

    start = '2020-01-18'
    end = '2020-01-19'
    device = '310'
    y_axis = ['Acc_magnitude_avg']
    local = False

    # Forms for user input
    aform = Chartinput(initial={'start': start, 'end': end, 'Local_Timezone': False})
    bform = Devicechoice(initial={'device': device})
    cform = Yaxischoice()
    context = {'aform': aform, 'bform': bform, 'cform': cform,}

    # If the user has submitted a form, use the values from the form
    if request.GET:
        values = request.GET
        start = str(values['start'])
        end = str(values['end'])
        device = str(values['device'])

        # handle deafult timezone selection as False
        if 'Local_Timezone' in values:
            local = values['Local_Timezone']
        else:
            local = False

        # Plot Axes Editting
        if 'y_axis' in values:
            y_axis = values.getlist('y_axis')
            print(y_axis)
            
    # Timezone Editting
    if local:
        data = Sensordata.objects.filter(sensor__sensor_number=device) # Return all objects with sensor_id to edit timezone
        time_label = f'Time ({data[0].timezone_offset})'# set graph labels
        for i in range(len(data)):
            data[i].UTC_Datetime = data[i].UTC_Datetime + timedelta(minutes=data[i].timezone_offset)

        # Create dt from string for list comprehension
        start = datetime.strptime(start, '%Y-%m-%d')
        end = datetime.strptime(end, '%Y-%m-%d') 

        data = [x for x in data if x.UTC_Datetime >= start and x.UTC_Datetime <= end]  # Refilter with python list since Django QuerySet would just rehit the db and mess up the timezone
        data.sort(key=lambda x: x.UTC_Datetime, reverse=True) # Makeshift orderby

        # DF for summary statistics
        df = pandas.DataFrame(data)

    else: # Query db to get filters data with default UTC
        data = Sensordata.objects.filter(sensor__sensor_number=device, UTC_Datetime__range=[start, end]).order_by('UTC_Datetime')
        if len(data) == 0:
            context['df_error'] = ' "\U0001F923" !!! No data found for this date range !!! "\U0001F923" '
            return render(request, 'main/main_page.html', context)
        time_label = 'UTC Time'

        # DF for summary statistics
        df = pandas.DataFrame(list(data.values()))


    # Continue summary statistics
    df_stats = df.describe(include='all', datetime_is_numeric=True)
    df_stats = style_df(df_stats)
    df_html = df_stats.to_html()
    context['df'] = df_html

    # Forms for user input
    aform = Chartinput(initial={'start': start, 'end': end, 'Local_Timezone': False})
    bform = Devicechoice(initial={'device': device})
    cform = Yaxischoice()
    context = {'aform': aform, 'bform': bform, 'cform': cform, 'df': df_html}
    
    # Create charts

    if y_axis:
        fig = make_subplots(rows = len(y_axis), cols = 1, shared_xaxes=True, vertical_spacing=0.05, subplot_titles=[str(x) for x in y_axis]) # create dynamic subplots

        for index, each in enumerate(y_axis):

            if each in ['Acc_magnitude_avg', 'eda_avg', 'Temp_avg', 'movement_intensity']: # create line charts for these variables

                fig.append_trace(go.Line(
                    x=[xvar.UTC_Datetime for xvar in data],
                    y=[getattr(yvar, each) for yvar in data],
                ), row=index + 1, col=1)

            elif each in ['Steps', 'rest', 'on_wrist']: # create bar charts for these variables
                fig.append_trace(go.Bar(
                    x=[xvar.UTC_Datetime for xvar in data],
                    y=[getattr(yvar, each) for yvar in data],
                ), row=index + 1, col=1)
            if index == len(y_axis) - 1:
                fig.update_xaxes(title_text=time_label, row=index + 1, col=1)

        fig.update_layout(height=1200, width=1200, title_text="Sensor Data", legend_title_text='Variables', ) # update layout for all charts to match css styling
        fig.update_layout(
            font_family='Arial, sans-serif',
            font_size=16,
            font_color='white',
            plot_bgcolor='white',
            paper_bgcolor='#262626',
        )
        fig.update_yaxes(
            gridcolor='darkgrey',
            linecolor='black',
            showline=True,
            ticks='outside',
        )
        fig.update_xaxes(
            gridcolor='darkgrey',
            linecolor='black',
            showline=True,
            ticks='outside',
        )
        chart = fig.to_html()
        context['chart'] = chart


    return render(request, 'main/main_page.html', context)

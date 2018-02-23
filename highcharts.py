views.py

from django.http import JsonResponse
from django.shortcuts import render
from ..models import Data
from unit.analysis_funcs import ChartData

def plot(request, chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
    data = ChartData.check_valve_data()

    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}  
    title = {"text": 'Check Valve Data'}
    xAxis = {"title": {"text": 'Serial Number'}, "categories": data['serial numbers']}
    yAxis = {"title": {"text": 'Data'}}
    series = [
        {"name": 'Mass (kg)', "data": data['mass']}, 
        {"name": 'Pressure Drop (psid)', "data": data['pressure drop']},
        {"name": 'Cracking Pressure (psid)', "data": data['cracking pressure']}
        ]

    return render(request, 'unit/data_plot.html', {'chartID': chartID, 'chart': chart,
                                                    'series': series, 'title': title, 
                                                    'xAxis': xAxis, 'yAxis': yAxis})



from unit.models import CheckValve

class ChartData(object):    
    def check_valve_data():
        data = {'serial numbers': [], 'mass': [],
                 'pressure drop': [], 'cracking pressure': [], 'reseat pressure': []}

        valves = CheckValve.objects.all()

        for unit in valves:
            data['serial numbers'].append(unit.serial_number)
            data['mass'].append(unit.mass)
            data['cracking pressure'].append(unit.cracking_pressure)
            data['pressure drop'].append(unit.pressure_drop)
            data['reseat pressure'].append(unit.reseat_pressure)

        return data   



{% extends "base.html" %}

{% block extrahead %}
    <!-- Load in jQuery and HighCharts -->
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="http://code.highcharts.com/highcharts.js"></script>
{% endblock %}

{% block heading %}
    <h1 align="center">Analysis</h1>
{% endblock %}

{% block content %}
    <div id={{ chartID|safe }} class="chart" style="height:100px; width:100%"></div>
{% endblock %}

{% block overwrite %}
<!-- Overwrite the base.html jQuery load and put in head for Highcharts to work -->
{% endblock %}

{% block extrajs %}
<!-- Maps the Python template context variables from views.py to the Highchart js variables -->
<script>
    var chart_id = {{ chartID|safe }}
    var chart = {{ chart|safe }}
    var title = {{ title|safe }}
    var xAxis = {{ xAxis|safe }}
    var yAxis = {{ yAxis|safe }}
    var series = {{ series|safe }}
</script>

<!-- Highchart js. Variable map shown above -->
<script>
$(document).ready(function() {
    $(chart_id).highcharts({
        chart: chart,
        title: title,
        xAxis: xAxis,
        yAxis: yAxis,
        series: series
    });
});
</script>
{% endblock %}




========

urls.py

from unit import views, graphs

urlpatterns = patterns('',

   url(r'^chart_data_json/', views.chart_data_json, name = 'chart_data_json'),

   url(r'^plot/', views.plot, name = 'plot'),

)
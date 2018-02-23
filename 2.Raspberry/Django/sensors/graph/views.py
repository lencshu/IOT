#!/usr/bin/env python
#-*- coding: utf-8 -*- 
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import ChartData

@csrf_exempt
def plot(request, chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
    datas = Data.objects.all()

    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}  
    title = {"text": 'Check Valve Data'}
    xAxis = {"title": {"text": 'Serial Number'}, "categories": datas['title']}
    yAxis = {"title": {"text": 'Data'}}
    series = [
        {"name": 'title', "data": datas['mass']}, 
        {"name": 'Pressure Drop (psid)', "data": datas['pressure drop']},
        {"name": 'Cracking Pressure (psid)', "data": datas['cracking pressure']}
        ]

    return render(request, 'unit/data_plot.html', {'chartID': chartID, 'chart': chart,
                                                    'series': series, 'title': title, 
                                                    'xAxis': xAxis, 'yAxis': yAxis})
#!/usr/bin/env python
#-*- coding: utf-8 -*- 
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def plot(request):
    return JsonResponse(data_list,safe=False)
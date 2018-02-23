# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.
import json
from django.shortcuts import render, get_object_or_404 
from .models import Data
from django.http import JsonResponse

def data_list(request):
    posts = {'title': [], 'distance': [],
                 'temperature': [], 'humity': [], 'light': []}
                 
    valves = Data.objects.all() 
    for unit in valves:
            posts['title'].append(unit.title)
            posts['distance'].append(unit.distance)
            posts['temperature'].append(unit.temperature)
            posts['humity'].append(unit.humity)
            posts['light'].append(unit.light)
    posts=JsonResponse(posts)
    # 而不是用json.dumps
    return render(request,'list.html',{'posts': posts})
    # return render(request,'list.html',{'posts': posts})

'''
def data_list(request):
    posts = Data.objects.all() 
    return render(request,'list.html',{'posts': posts})

'''
# def post_detail(request, year, month, day, post): 
#     post = get_object_or_404(Post,publish__year=year, 
#                                    publish__month=month, 
#                                    publish__day=day) 
#     return render(request, 
#                   'blog/post/detail.html', 
#                   {'post': post})


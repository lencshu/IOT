# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404 
from .models import Data

def data_list(request):
    posts = Data.objects.all() 
    return render(request,'list.html',{'posts': posts})


# def post_detail(request, year, month, day, post): 
#     post = get_object_or_404(Post,publish__year=year, 
#                                    publish__month=month, 
#                                    publish__day=day) 
#     return render(request, 
#                   'blog/post/detail.html', 
#                   {'post': post})


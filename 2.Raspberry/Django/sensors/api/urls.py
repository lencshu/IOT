#!/usr/bin/env python
#-*- coding: utf-8 -*- 
from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^api/$', views.data_list),
    url(r'^api/(?P<pk>[0-9]+)/$', views.data_detail),
]

'''
urlpatterns = [
    url(r'^subjects/$', 
        views.SubjectListView.as_view(), 
        name='subject_list'), 
    url(r'^subjects/(?P<pk>\d+)/$', 
        views.SubjectDetailView.as_view(), 
        name='subject_detail'),
    url(r'^post/(?P<pk>\d+)/$', 
        views.DataSave.as_view(),
        name='DataSave'),
]
'''
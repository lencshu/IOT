#!/usr/bin/env python
#-*- coding: utf-8 -*- 

from graphs.py import BarView
    url(regex='^bar/$', view=BarView.as_view(), name='bar')
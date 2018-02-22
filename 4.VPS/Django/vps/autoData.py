#!/usr/bin/env python
#-*- coding: utf-8 -*- 


import os,datetime,pytz
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vps.settings")
django.setup()

from sensors.models import Data
def parisnow():
    return datetime.datetime.now(tz=pytz.timezone("Europe/Paris")).isoformat()

timeDelay=0

import serial
import json

ser = serial.Serial('/dev/ttyACM0', 9600)
while ser.isOpen():
    rawLigne = ser.readline()
    #print len(rawLigne)
    try:
      tempeData = json.loads(rawLigne)
      if (tempeData["Triger"]):
        print tempeData
      else:
        if (tempeData["Humity"] != 0):
            timeDelay+=1
            if timeDelay>=10:
                print 'Saved to database'
                Data.objects.create(title=parisnow(), distance = tempeData["Distance"],temperature = tempeData["Temperature"],humity = tempeData["Humity"],light = tempeData["Light"])
                timeDelay=0
    except:
      # do nothing, not a valid JSON
      pass




"""
{
  "Triger": 0,
  "Time": 1504611032,
  "Distance": 5,
  "Temperature": 20,
  "Humity": 49,
  "Light": 103
}
{
  "Triger": 1,
  "IR": 0,
  "Swich": 1,
  "Stick": [
    499,
    510
  ]
}
"""




'''
# Data.save()
# 
# 
# 


# 
# print datetime.datetime.now().isoformat()
# print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S%Z")
# print datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
# from datetime import datetime

# import pytz # $ pip install pytz
# from tzlocal import get_localzone # $ pip install tzlocal

# now = datetime.datetime.now().isoformat()
# print now
# tz = get_localzone()
# print datetime.datetime.now().strftime("%z")
# local_dt = tz.localize(now, is_dst=None)
# utc_dt = local_dt.astimezone(pytz.utc) #NOTE: utc.normalize() is unnecessary here
# print now,tz
# print local_dt

# YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]



import django
# from django.conf import settings
# import os

# from ..vps import settings
# os.environ['DJANGO_SETTINGS_MODULE'] ='..vps.settings'
# django.setup()

# settings.configure(default_settings=vps_defaults, DEBUG=True)
# django.setup()

# import vps.sensors.models
# import models


import importlib
module_name = 'Data'
Data = importlib.import_module(module_name, package='models')


# import sys,os
# from datetime import *
# # sys.path.append('/www/web/')
# from vps.vps import settings



'''
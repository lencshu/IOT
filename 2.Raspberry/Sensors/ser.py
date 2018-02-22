#!/usr/bin/env python
#-*- coding: utf-8 -*- 

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
          print tempeData["Humity"]
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

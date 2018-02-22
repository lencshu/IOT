#!/usr/bin/env python
#-*- coding: utf-8 -*- 

import requests
url = "http://127.0.0.1:8000/api/"
payload = '{"title": "2018-02-20T23:52:16.202497+01:00", "distance": 2, "temperature": 16, "humity": 37, "light": 47}'
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    'Postman-Token': "64fb7111-5dfd-de0d-cc5e-eb4c063a9486"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
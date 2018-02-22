## 4.4 Django 框架

### 4.4.1 初始化

- 安装各种框架

~~~python hl_lines="1"
#最后支持py2.7的版本
pip install Django==1.11.10

#Restful API
pip install djangorestframework
pip install markdown
# Filtering support
pip install django-filter

#mongodb database
pip install mongoengine

#PY time zone
pip install pytz
~~~

- 创建项目和app

~~~python hl_lines="1"
django-admin startproject pi
python manage.py startapp sensors

# 管理员用户
python manage.py createsuperuser
~~~

- 初始化数据库链表

~~~python hl_lines="1"
python manage.py migrate
~~~

- 初始化app链表

~~~python hl_lines="1"
python manage.py makemigrations sensors
~~~


!!! hint ""
    If you ：
    - edit your models.py file in order to add, remove, 
    - change fields of existing models, 
    - add new models, 
    You will have to: 
    - 1. make a new migration using the `python manage.py makemigrations sensors`. The migration will allow Django to keep track of model changes. 
    - 2. Then you will have to apply it with the `python manage.py migrate` to keep the database in sync with your models.


- 运行调试

~~~python hl_lines="1"
python manage.py runserver
python manage.py shell
~~~

curl.exe -u lencshu:169088@Dj -X POST -d "temperature=1&distance=1" http://127.0.0.1:8000/api/subjects/

### 4.4.2 配置项目

~~~python hl_lines="1 13 16"
#apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'sensors',
]

#Timezone
TIME_ZONE = 'Europe/Paris'

#Restframework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
~~~

### 4.4.3 App配置

**models.py**

~~~python hl_lines="1"
# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.db import models

# Create your models here.

from django.utils import timezone
# from django.contrib.auth.models import User
class Data(models.Model):
    title = models.DateTimeField(default=timezone.now)
    distance = models.IntegerField()
    temperature = models.IntegerField()
    humity = models.IntegerField()
    light = models.IntegerField()
    class Meta:
        ordering = ('-title','-temperature')
~~~

**views.py**

~~~python hl_lines="1"
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404 
from .models import Data

def data_list(request):
    posts = Data.objects.all() 
    return render(request,'list.html',{'posts': posts})
~~~

**模板配置—list.html&base.html**

**base.html**

~~~python hl_lines="1"
{% load staticfiles %}
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}{% endblock %}</title>
  <link href="{% static "css/blog.css" %}" rel="stylesheet"> 
</head>
<body>
  <div id="content">
    {% block content %}
    {% endblock %}
  </div>
  <div id="sidebar">
    <h2>Sensors data listing</h2>
      <p>From Arduino-raspberry</p>
  </div>
</body>
</html>
~~~

**list.html**

~~~html hl_lines="1"
{% extends "base.html" %}
{% block title %}My Blog{% endblock %}
{% block content %}
  <h1>Datas</h1>
  {% for post in posts %}
    <h4>{{ post.title }}</h4>
    <p class="date">
      Temperature: {{ post.temperature }} <p>
      Humity: {{ post.humity }} <p>
      Light: {{ post.light }} <p>
      Distance: {{ post.distance }} <p>
    </p>
    {{ post.body|truncatewords:30|linebreaks }}
  {% endfor %}
{% endblock %}
~~~

**配置—urls.py**

**App Urls**

~~~python hl_lines="1"
from django.conf.urls import url 
from . import views

urlpatterns = [
    # post views
        url(r'^$', views.data_list, name='data_list'), 
]
~~~

**项目urls**

~~~python hl_lines="1"
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^s/', include('sensors.urls',namespace='sensors',app_name='sensors')),
    url(r'^api/', include('sensors.api.urls', namespace='api')),
]
~~~

**配置admin.py**

~~~python hl_lines="1"
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('title', 'distance', 'temperature', 'humity', 'light')
    date_hierarchy = 'title'
    ordering = ['-title','-temperature']

admin.site.register(Data, DataAdmin)
~~~

### 4.4.4 RESTful API

**Views**

~~~python hl_lines="1"
#!/usr/bin/env python
#-*- coding: utf-8 -*- 
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ..models import Data
from .serializers import SubjectSerializer

@csrf_exempt
def data_list(request):
    # List all code snippets, or create a new data.
    if request.method == 'GET':
        datas = Data.objects.all()
        serializer = SubjectSerializer(datas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def data_detail(request, pk):
    # Retrieve, update or delete a code datas.
    try:
        datas = Data.objects.get(pk=pk)
    except Data.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SubjectSerializer(datas)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(datas, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        datas.delete()
        return HttpResponse(status=204)
~~~

**序列化**

~~~python hl_lines="1"

from rest_framework import serializers 
from ..models import Data
import os,datetime,pytz
from django.utils import timezone

# def parisnow():
    # return datetime.datetime.now(tz=pytz.timezone("Europe/Paris")).isoformat()1

class SubjectSerializer(serializers.Serializer): 
    id = serializers.IntegerField(read_only=True)
    title = serializers.DateTimeField(required=False)
    distance = serializers.IntegerField()
    temperature = serializers.IntegerField()
    humity = serializers.IntegerField()
    light = serializers.IntegerField()

    def create(self, validated_data):
        #Create and return a new `Subject` instance, given the validated data.
        return Data.objects.create(**validated_data)

    def update(self, instance, validated_data):

        # Update and return an existing `Snippet` instance, given the validated data.
        instance.title = validated_data.get('title', instance.title)
        # instance.title = validated_data.get('title', parisnow())
        instance.distance = validated_data.get('distance', instance.distance)
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.humity = validated_data.get('humity', instance.humity)
        instance.light = validated_data.get('light', instance.light)
        instance.save()
        return instance

~~~

**URLs**

~~~python hl_lines="1"
from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^api/$', views.data_list),
    url(r'^api/(?P<pk>[0-9]+)/$', views.data_detail),
]
~~~

### 4.4.5 与Arduino对接

~~~python hl_lines="1"
#!/usr/bin/env python
#-*- coding: utf-8 -*- 

import os,datetime,pytz
import django
import serial
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pi.settings")
django.setup()

from sensors.models import Data
def parisnow():
    return datetime.datetime.now(tz=pytz.timezone("Europe/Paris")).isoformat()

timeDelay=0

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
~~~

### 4.4.6 与vps对接

数据格式
`{"title": "2018-02-20T23:49:16.202497+01:00", "distance": 2, "temperature": 16, "humity": 37, "light": 47}`

~~~python hl_lines="1"

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
~~~

### 4.4.7 图表



### 4.4.2 部署
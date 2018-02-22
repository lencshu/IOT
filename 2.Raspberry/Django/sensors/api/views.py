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





"""
from rest_framework import generics
from ..models import Data
from .serializers import SubjectSerializer

from django.shortcuts import get_object_or_404 
from rest_framework.views import APIView
from rest_framework.response import Response

class SubjectListView(generics.ListAPIView): 
    queryset = Data.objects.all() 
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView): 
    queryset = Data.objects.all() 
    serializer_class = SubjectSerializer

class DataSave(APIView):
    def post(self, request, pk, format=None): 
        Data = get_object_or_404(Data, pk=pk) 
        Data.add(request) 
        return Response({'DataSaved': True})
"""





"""
from rest_framework import generics
from ..models import Data
from .serializers import SubjectSerializer

from django.shortcuts import get_object_or_404 
from rest_framework.views import APIView
from rest_framework.response import Response

class SubjectListView(generics.ListAPIView): 
    queryset = Data.objects.all() 
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView): 
    queryset = Data.objects.all() 
    serializer_class = SubjectSerializer

class DataSave(APIView):
    def post(self, request, pk, format=None): 
        Data = get_object_or_404(Data, pk=pk) 
        Data.add(request) 
        return Response({'DataSaved': True})
"""

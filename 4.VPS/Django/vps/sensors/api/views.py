from rest_framework import generics
from ..models import Data
from .serializers import SubjectSerializer

class SubjectListView(generics.ListAPIView): 
    queryset = Data.objects.all() 
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView): 
    queryset = Data.objects.all() 
    serializer_class = SubjectSerializer
 

from django.shortcuts import get_object_or_404 
from rest_framework.views import APIView
from rest_framework.response import Response

class DataSave(APIView):
    def post(self, request, pk, format=None): 
        Data = get_object_or_404(Data, pk=pk) 
        Data.add(request) 
        return Response({'DataSaved': True})
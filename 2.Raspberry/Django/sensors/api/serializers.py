#!/usr/bin/env python
#-*- coding: utf-8 -*- 
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


'''
class SubjectSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Data
        fields = '__all__'
        '''
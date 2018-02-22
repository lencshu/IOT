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
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

    # def get_absolute_url(self):
    #     return reverse('blog:post_detail', 
    #                    args=[self.publish.year, 
    #                          self.publish.strftime('%m'), 
    #                          self.publish.strftime('%d'), 
    #                          self.slug])

'''        
    objects = models.Manager() # The default manager. 
    published = PublishedManager() # Our custom manager.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

    # slug = models.SlugField(max_length=250,unique_for_date='title') 
        
'''
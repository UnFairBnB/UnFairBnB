# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe

AREA_CHOICES = (
    ('area1','AREA1'),
    ('area2','AREA2'),
)

TYPE_CHOICES = (
    ('type1','type1'),
    ('type2','type2'),
)

YES_NO_CHOICES = (
    ('yes','yes'),
    ('no','no'),
)

class Appartment(models.Model):
  area = models.CharField(max_length=6, choices=AREA_CHOICES, default='area1')
  acommodates = models.IntegerField(max_length=2, default=1) 
  bathrooms = models.IntegerField(max_length=2, default=1)
  bedrooms = models.IntegerField(max_length=2, default=1)
  type = models.CharField(max_length=6, choices=TYPE_CHOICES, default='type1')
  private = models.CharField(max_length=3, choices=YES_NO_CHOICES)
  wifi = models.CharField(max_length=3, choices=YES_NO_CHOICES)
  TV = models.CharField(max_length=3, choices=YES_NO_CHOICES)
  lock = models.CharField(max_length=3, choices=YES_NO_CHOICES)
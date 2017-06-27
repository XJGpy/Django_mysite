# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=100)


class Tag(models.Model):
	name = models.CharField(max_length=100)

class post(models.Model):
	title = models.CharField(max_length=70)
	
	body = models.TextFirld()
	
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()

	excerpt = models.CharField(max_length=200, blank=True)
	
	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag, blank=True)

	author = models.ForeignKey(User)


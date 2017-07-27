# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone


@python_2_unicode_compatible
class Category(models.Model):
	"""
	Model for news categories 

	"""
	name = models.CharField(max_length=128) 
	slug = models.SlugField(max_length=200, db_index=True, unique=True)


	class Meta: 
		ordering = ['name']
		verbose_name = 'Category' 
		verbose_name_plural = 'Categories' 

	def __str__(self): 
		return '{0}'.format(self.name)


@python_2_unicode_compatible
class News(models.Model):
	"""
	Model for news 

	"""
	category = models.ForeignKey('Category', related_name='news')
	image = models.ImageField()
	author_image = models.CharField(max_length=200, verbose_name='Author Image')
	title = models.CharField(max_length=200, verbose_name='Title')
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	important = models.BooleanField(default=False)


	class Meta:
		ordering = ['-created_date']
		verbose_name = 'News' 
		verbose_name_plural = 'News' 


	def __str__(self):
		return '{0} | {1}'.format(self.category, self.title)
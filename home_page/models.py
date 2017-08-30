# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone

from mptt.models import MPTTModel, TreeForeignKey

@python_2_unicode_compatible
class Category(MPTTModel):
	"""
	Model for news categories

	"""
	name = models.CharField(max_length=128, unique=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

	class MPTTMeta:
		order_insertion_by = ['name']

	def __str__(self):
		return '{0}'.format(self.name)


@python_2_unicode_compatible
class News(models.Model):
	"""
	Model for news

	"""
	category = models.ForeignKey('Category', related_name='news')
	image = models.ImageField()
	author_image = models.CharField(
		max_length=200,
		verbose_name='Author Image'
	)
	title = models.CharField(max_length=200, verbose_name='Title')
	additional_title = models.CharField(
		max_length=200,
		verbose_name='Additional Title'
	)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	important = models.BooleanField(default=False)

	class Meta:
		ordering = ['-created_date']
		verbose_name = 'News'
		verbose_name_plural = 'News'

	def __str__(self):
		return '{0} | {1}'.format(self.category, self.title)

	def get_absolute_url(self):
		year = created_date.year
		month = created_date.month
		day = created_date.day
		return reverse_lazy('home_page:detail', kwargs={
							'slug': self.slug,
							'year': '{}'.format(year),
							'month': '{}'.format(month),
							'day': '{}'.format(day),
						})

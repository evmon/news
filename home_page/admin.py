# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import News, Category


class CategoryAdmin(admin.ModelAdmin):
	"""
	Category model
	list_display: fields listed in list_editable will be displayed as form widgets on the change list page
	prepopulated_fields: the generated value is produced by concatenating the values of the source fields

	"""
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

class NewsAdmin(admin.ModelAdmin):
	"""
	News model
	list_display: fields listed in list_editable will be displayed as form widgets on the change list page
	prepopulated_fields: the generated value is produced by concatenating the values of the source fields
	
	"""
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Max
from django.views.generic import ListView
from datetime import datetime, timedelta, time, date
from django.template import defaultfilters
from .models import Category, News
import base64
from django.contrib.auth import authenticate, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User

# from django.contrib.auth.decorators import login_required



# @login_required
class NewsView(ListView):

	model = News

	def get_context_data(self, **kwargs):

		context = super(NewsView, self).get_context_data(**kwargs)
		categories = Category.objects.all()
		all_news = News.objects.all().order_by('-created_date')
		all_news_today = all_news.filter(created_date__date=date.today())
		imp_news = all_news.filter(important="True").order_by('-created_date')
		imp_news_sort = imp_news.order_by('created_date')
		unimp_news = all_news_today.filter(important="False")
		yesterday = date.today() - timedelta(days=1)
		all_news_yest = all_news.filter(created_date__date=yesterday)
		imp_news_yest = all_news_yest.filter(important="True")
		
		context = {
			'imp_news': imp_news,
			'imp_news_sort': imp_news_sort,
			'unimp_news': unimp_news,
			'imp_news_yesterday': imp_news_yest,
			'categories': categories,
			'all_news': all_news_today,
		}
		
		return context


def base_auth(request):

	if request.user.is_authenticated():
		return redirect('home_page:home')

	if 'HTTP_AUTHORIZATION' in request.META:

		auth = request.META['HTTP_AUTHORIZATION'].split()
		
		if len(auth) == 2:

			if auth[0].lower() == "basic":

				uname, passwd = base64.b64decode(auth[1]).split(':')

				user = authenticate(request, username=uname, password=passwd)

				if user is not None and user.is_superuser:
					login(request)
					request.user = user
					
					return redirect('home_page:home')

	response = HttpResponse()
 	response.status_code = 401
	response['WWW-Authenticate'] = 'Basic realm="%s"' % "Basic Auth Protected"
    
	return response
    

"""news URL Configuration

The `urlpatterns` list routes URLs to views. 
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('home_page.urls')),
]

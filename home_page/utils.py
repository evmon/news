# -*- coding: utf-8 -*-
import time

from django.utils import timezone

from home_page.models import News


def initial_date_data(initial, *args, **kwargs):
    if not initial:
        print('''Сhange value of all dates for news
                 available arguments:
                 --initial \t Set initial values for all dates''')
        return False

    if initial:
        print('Setting initial values for date for news')
        for item in News.objects.all():
            date = timezone.now()
            item.created_date = item.created_date.replace(
                year=date.year,
                month=date.month,
                day=date.day,
            )
            print('Saving... Item ID: {0:5d}'.format(item.id))
            item.save(update_fields=['created_date', ])
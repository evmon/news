# -*- coding: utf-8 -*-
from django.core.management import BaseCommand, CommandError

from home_page.utils import initial_date_data

class Command(BaseCommand):
    help = 'Сhange value of all dates for news'

    def add_arguments(self, parser):
        parser.add_argument(
            '--initial',
            dest='initial',
            action='store_true',
            default=False,
            help='Set initial values of all dates for news'
        )

    def handle(self, *args, **options):
        """
        manage.py will run this function
        """
        try:
            initial_date_data(**options)
        except Exception as e:
            raise CommandError('An error has occurred: {}'.format(e))


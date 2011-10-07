from django.core.management.base import BaseCommand, CommandError
from django.db import models

class Command(BaseCommand):
    args = ''
    help = 'get list of models and its objects quantity'

    def handle(self, *args, **options):
       pass

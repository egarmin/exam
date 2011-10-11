from django.core.management.base import BaseCommand
from django.db import models


class Command(BaseCommand):
    args = ''
    help = 'get list of models and its objects quantity'

    def handle(self, *args, **options):
        models_list = models.get_models()
        self.stdout.write('There are %s models. Notably:\n' % len(models_list))
        self.stderr.write('error: There are %s models. Notably:\n' %
                          len(models_list))
        for model in models_list:
            n = model.objects.count()
            model_name = str(model).split('\'')[1]
            self.stdout.write(('%s has %s object(s)\n' %
                               (model_name, n)).lower())
            self.stderr.write(('error: %s has %s object(s)\n' %
                               (model_name, n)).lower())

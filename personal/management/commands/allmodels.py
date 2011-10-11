from django.core.management.base import BaseCommand
from django.db import models
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    args = ''
    help = 'get list of models and its objects quantity'

    def handle(self, *args, **options):

        models_list = models.get_models()
        out = 'There are %s models. Notably:\n' % len(models_list)
        for model in models_list:
            n = model.objects.count()
            model_name = str(model).split('\'')[1]
            out += '%s has %s object(s)\n' % (model_name, n)
        self.stdout.write('%s' % out)
        self.stderr.write('ERROR:\n%s' % out)

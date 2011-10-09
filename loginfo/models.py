# -*- coding: utf-8 -*-
from django.db import models
from django.db.utils import DatabaseError
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save, post_delete
from django.contrib.contenttypes.models import ContentType


class LogRequest(models.Model):
    added = models.DateTimeField(auto_now_add=True,
                                 verbose_name=_('was added'))
    path = models.TextField(verbose_name=_('path'))
    content = models.TextField(verbose_name=_('parameters'))
    user_info = models.TextField(verbose_name=_('user info'))
    priority = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return "%s: %s" % (self.pk, self.path)


class LogModel(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=10)
    app_name = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    id_obj = models.CharField(max_length=20)


def my_handler(sender, **kwargs):
    obj = kwargs['instance']
    obj_instance = ContentType.objects.get_for_model(obj)
    if obj_instance.model_class() is LogModel:
        return
    if kwargs['signal'] == post_save:
        if kwargs['created']:
            action = 'create'
        else:
            action = 'change'
    else:
        action = 'delete'

    if hasattr(obj, 'id'):
        id_obj = str(obj.id)
    else:
        id_obj = 'absent'
    rec = LogModel(app_name=obj_instance.app_label,
                   model_name=obj_instance.model,
                   id_obj = id_obj,
                   action=action)
    try:
        rec.save()
    except DatabaseError:
        print 'The signal from %s was not saved.' % str(sender)
    return


post_save.connect(my_handler)
post_delete.connect(my_handler)

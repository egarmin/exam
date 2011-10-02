# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class LogRequest(models.Model):
    added = models.DateTimeField(auto_now_add=True, verbose_name=_('was added'))
    path = models.TextField(verbose_name=_('full path'))
    is_secure = models.CharField(max_length=6, verbose_name=_('secured'))
    is_ajax = models.CharField(max_length=6, verbose_name=_('via ajax'))
    content = models.TextField(verbose_name=_('parameters'))
    user_info = models.TextField(verbose_name=_('user info'))

    def __unicode__(self):
        return "%s: %s" % (self.pk, self.path)

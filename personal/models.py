# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    name = models.CharField(max_length=25, verbose_name=_('name'))
    surname = models.CharField(max_length=25, verbose_name=_('surname'))
    bio = models.TextField(verbose_name=_('biography'), blank=True)
    birthday = models.DateField(verbose_name=_('birthday'), blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name=_('phone'), blank=True)
    email = models.CharField(blank=True, max_length=45, verbose_name=_('e-mail'))

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')

    def __unicode__(self):
        return '%s %s'% (self.name, self.surname)

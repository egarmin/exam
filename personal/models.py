# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    name = models.CharField(max_length=25, verbose_name=_('name'))
    surname = models.CharField(max_length=25, verbose_name=_('surname'))
    birthday = models.DateField(verbose_name=_('date of birth'),
                                blank=True, null=True)
    bio = models.TextField(verbose_name=_('biography'), blank=True)
    jid = models.EmailField(blank=True, verbose_name=_('jabber'))
    skype = models.CharField(max_length=55, blank=True,
                             verbose_name=_('skype'))
    email = models.EmailField(blank=True, verbose_name=_('e-mail'))
    appendix = models.TextField(verbose_name=_('appendix'), blank=True)

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('people')

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)

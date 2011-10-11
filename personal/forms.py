# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
import settings

from personal.models import Person


class CalendarWidget(forms.DateInput):
    """ Widget for Сalendar
    """
    class Media:
        js = ('/jsi18n/',
                settings.ADMIN_MEDIA_PREFIX + 'js/core.js',
                settings.ADMIN_MEDIA_PREFIX + 'js/calendar.js',
                settings.ADMIN_MEDIA_PREFIX + 'js/admin/DateTimeShortcuts.js')
        css = {
            'all': (
                settings.ADMIN_MEDIA_PREFIX + 'css/widgets.css',
            )
        }

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(attrs={'class': 'vDateField',
                                                    'size': '12'})


class PersonForm(forms.ModelForm):

    birthday = forms.DateField(input_formats=["%d.%m.%Y", "%Y-%m-%d"],
                               label=_("Date of birth:"), required=False,
                               widget=CalendarWidget)
    bio = forms.CharField(label=_('Biography:'), required=False,
                    widget=forms.Textarea(attrs={'cols': '35', 'rows': '6'}))
    appendix = forms.CharField(label=_('Appendix:'), required=False,
                    widget=forms.Textarea(attrs={'cols': '35', 'rows': '6'}))

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        rev = []
        index = len(self.fields.keyOrder) / 2
        order = self.fields.keyOrder
        rev = order[index:] + order[:index]
        rev.reverse()
        self.fields.keyOrder = rev

    class Meta:
        model = Person

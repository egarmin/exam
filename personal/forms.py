# -*- coding: utf-8 -*-
from django.forms import DateInput, ModelForm, Textarea
import settings

from personal.models import Person


class CalendarWidget(DateInput):
    """ Widget for Сalendar  """
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


class PersonForm(ModelForm):
    class Meta:
        model = Person
        widgets = {
            'bio': Textarea(attrs={'cols': 35, 'rows': 6}),
            'appendix': Textarea(attrs={'cols': 35, 'rows': 6}),
            'birthday': CalendarWidget(),
            }

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        index = len(self.fields.keyOrder) / 2
        order = self.fields.keyOrder
        rev = order[index:] + order[:index]
        rev.reverse()
        self.fields.keyOrder = rev

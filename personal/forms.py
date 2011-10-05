# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from django.forms.formsets import formset_factory


class PersonForm(forms.Form):
    name = forms.CharField(max_length=50, label=_('Name'),
                 error_messages={'required': _("Enter your surname, please")})
    surname = forms.CharField(max_length=50, label=_('Surname'),
                 error_messages={'required': _("Enter your surname, please")})
    birthday = forms.DateField(input_formats=["%d.%m.%Y", "%Y-%m-%d"],
                               label=_("Birthday"), required=False)
    bio = forms.CharField(label=_('Biography'), required=False,
                    widget=forms.Textarea(attrs={'cols': '35', 'rows': '6'}))


class ContactForm(forms.Form):
    email = forms.EmailField(max_length=50, label=_("Email"), required=False)
    jid = forms.EmailField(max_length=50, label=_('Jabber'), required=False)
    skype = forms.CharField(max_length=13, label=_('Skype'), required=False)
    appendix = forms.CharField(label=_('Appendix'), required=False,
                    widget=forms.Textarea(attrs={'cols': '35', 'rows': '6'}))

# -*- coding: utf-8 -*-
from django.contrib import admin
from personal.models import Person, Contacts


class ContactsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'email', 'jid', 'skype']
    list_display_links = ['pk']
    list_per_page = 50
    search_fields = ['name', 'surname']
    ordering = ['id']


class PersonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'surname', 'birthday']
    list_display_links = ['name']
    list_per_page = 50
    search_fields = ['name', 'surname']
    ordering = ['id']


admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Person, PersonAdmin)


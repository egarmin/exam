# -*- coding: utf-8 -*-
from django.contrib import admin
from personal.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'surname', 'birthday']
    list_display_links = ['name']
    list_per_page = 50
    search_fields = ['name', 'surname']
    ordering = ['id']

admin.site.register(Person, PersonAdmin)
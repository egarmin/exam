# -*- coding: utf-8 -*-
from django.contrib import admin
from personal.models import Person


class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)

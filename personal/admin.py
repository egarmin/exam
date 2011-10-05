# -*- coding: utf-8 -*-
from django.contrib import admin
from personal.models import Person, Contacts


class ContactInline(admin.StackedInline):
    model = Contacts
    extra = 1


class PersonAdmin(admin.ModelAdmin):
    inlines = [ContactInline]


admin.site.register(Person, PersonAdmin)

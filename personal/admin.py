# -*- coding: utf-8 -*-
from django.contrib import admin
from personal.models import Person, Contacts


class ContactAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Contacts, ContactAdmin)

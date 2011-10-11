# -*- coding: utf-8 -*-
from django.contrib import admin

from loginfo.models import LogModel, LogRequest


class LogModelsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'added', 'app_name', 'model_name',
                    'id_obj', 'action']
    list_display_links = ['pk']
    list_per_page = 50
    search_fields = ['model_name', 'action']
    ordering = ['id']


class LogRequestAdmin(admin.ModelAdmin):
    list_display = ['pk', 'added', 'path']
    list_display_links = ['pk']
    list_per_page = 50
    search_fields = ['path']
    ordering = ['added']


admin.site.register(LogModel, LogModelsAdmin)
admin.site.register(LogRequest, LogRequestAdmin)

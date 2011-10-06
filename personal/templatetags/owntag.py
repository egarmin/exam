# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.simple_tag
def admin_link(arg):
    if hasattr(arg, '_meta'):
        app = arg._meta.app_label
        module = arg._meta.module_name
    elif hasattr(arg, 'model'):
        app = arg.model._meta.app_label
        module = arg.model._meta.module_name
    else:
        error = "The elink's argument must be a model or QuerySet. %s isn't a model." % arg
        raise template.TemplateSyntaxError(error)
    res_link = '/admin/%s/%s/' % (app, module)
    if hasattr(arg, 'id'):
        res_link += '%s/' % arg.id
    return res_link

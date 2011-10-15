# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag
def admin_link(arg):
    if hasattr(arg, '_meta'):
        app = arg._meta.app_label
        module = arg._meta.module_name
        res_link = reverse('admin:%s_%s_change' % (app, module),
                           args=(arg.id,))
    else:
        error = "Wrong argument of admin_link tag. Must be an object."
        raise template.TemplateSyntaxError(error)
    return res_link

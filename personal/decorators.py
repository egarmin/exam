# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

def render_to(template=None, mimetype="text/html"):
    """
    Decorator for Django views that sends returned dict to render_to_response
    function.
    """
    def renderer(function):
        def wrapper(request, *args, **kwargs):
            output = function(request, *args, **kwargs)
            if not isinstance(output, dict):
                return output
            tmpl = output.pop('TEMPLATE', template)
            return render_to_response(tmpl, output, \
                        context_instance=RequestContext(request), mimetype=mimetype)
        return wrapper
    return renderer


# -*- coding: utf-8 -*-
from personal.decorators import render_to
from loginfo.models import LogRequest


@render_to('display_req.html')
def display_requests(request):
    try:
        req_list = LogRequest.objects.all().order_by('added')[0:10]
    except:
        req_list = None
    return {'req_list': req_list}

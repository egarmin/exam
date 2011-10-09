# -*- coding: utf-8 -*-
from personal.decorators import render_to
from loginfo.models import LogRequest


@render_to('display_req.html')
def display_requests(request):
    req_list = LogRequest.objects.all().order_by('-priority', 'added')[:10]
    return {'req_list': req_list}

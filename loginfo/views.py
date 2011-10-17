# -*- coding: utf-8 -*-
from loginfo.models import LogRequest
from personal.decorators import render_to


arr = {'pk': '&nbsp;',
       'added': '&darr;',  # default
       'priority': '&nbsp;',
       'path': '&nbsp;',
       '&uarr;': '&darr;',
       '&darr;': '&uarr;',
       'last': 'added',  # default
       'order': False}   # default


@render_to('display_req.html')
def display_requests(request):

    main_field = request.GET.get('field')
    sign = ['', '-']
    if main_field in arr:
        if arr['last'] == main_field:
            arr['order'] = not arr['order']
            arr[main_field] = arr[arr[main_field]]
        else:
            arr['order'] = False
            arr[arr['last']] = '&nbsp'
            arr[main_field] = '&darr;'
            arr['last'] = main_field
    req_list = LogRequest.objects.all().order_by(sign[arr['order']]
                                               + arr['last'])[:10]
    return {'req_list': req_list, 'arr': arr}

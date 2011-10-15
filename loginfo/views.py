# -*- coding: utf-8 -*-
from loginfo.models import LogRequest
from personal.decorators import render_to


arr = {'pk': '&nbsp;',
       'added': '&nbsp;',
       'priority': '&nbsp;',
       'path': '&nbsp;',
       '&uarr;': '&darr;',
       '&darr;': '&uarr;',
       'last': '',
       'order': True}


@render_to('display_req.html')
def display_requests(request):

    main_field = request.GET.get('field')
    if not main_field:
        if arr['last'] != '':
            arr[arr['last']] = '&nbsp;'
            arr['last'] = ''
        req_list = LogRequest.objects.all().order_by('added')[:10]
    else:
        sign = ['', '-']
        if arr['last'] == main_field:
            s = not arr['order']
            arr['order'] = s
            arr[main_field] = arr[arr[main_field]]
        else:
            s = False
            arr['order'] = False
            if arr['last'] != '':
                arr[arr['last']] = '&nbsp'
            arr[main_field] = '&darr;'
            arr['last'] = main_field
        req_list = LogRequest.objects.all().order_by(sign[int(s)]
                                               + main_field)[:10]
    return {'req_list': req_list, 'arr': arr}

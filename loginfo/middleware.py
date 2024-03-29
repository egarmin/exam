# -*- coding: utf-8 -*-
from loginfo.models import LogRequest


def make_text(inp_dict):
    values = inp_dict.items()
    values.sort()
    if not values:
        return '\nno data'
    out_text = []
    for k, v in values:
        out_text.append('\n%s = %s' % (k, v))
    return ''.join(out_text)


class MyMiddle:

    def process_request(self, request):
        if 'middle' in request.path or 'admin' in request.path:
            return
        new_rec = LogRequest()
        req_text = '\n*******COMMON INFO*********'
        req_text += '\nmethod = %s' % request.method
        req_text += '\nsecure = \'%s\'' % str(request.is_secure())
        req_text += '\najax = \'%s\'' % str(request.is_ajax())
        req_text += '\npath_info = \'%s\'' % request.path_info
        req_text += '\nsession_key = %s' % request.session.session_key
        req_text += '\n******* META section *********'
        req_text += make_text(request.META)
        req_text += '\n******* COOKIES section *********'
        req_text += make_text(request.COOKIES)
        req_text += '\n******* POST section *********'
        req_text += make_text(request.POST)
        req_text += '\n******* GET section *********'
        req_text += make_text(request.GET)
        req_text += '\n******* REQUEST section *********'
        req_text += make_text(request.REQUEST)
        req_text += '\n******* FILES section *********'
        req_text += make_text(request.FILES)
        if request.user.username is '':
            user_text = '\nusername = %s' % 'AnonymousUser'
        else:
            user_text = '\nusername = %s' % request.user.username
            user_text += '\npassword = %s' % request.user.password
            user_text += '\ne-mail = %s' % request.user.email
            user_text += '\nfirst_name = %s' % request.user.first_name
            user_text += '\nlast_name = %s' % request.user.last_name
            user_text += '\nis active = %s' % str(request.user.is_active)
            user_text += '\nis staff = %s' % str(request.user.is_staff)
            user_text += '\nis superuser = %s' % str(request.user.is_superuser)
        new_rec.content = req_text
        new_rec.user_info = user_text
        new_rec.path = request.path
        new_rec.save()

# -*- coding: utf-8 -*-
from loginfo.models import LogRequest


class MyMiddle:

    def process_request(self, request):
        new_rec = LogRequest()
        req_text = '\n*******COMMON INFO*********'
        req_text += '\nmethod = %s' % request.method
        req_text += '\npath_info = \'%s\'' % request.path_info
        req_text += '\nraw_post_data = \'%s\'' % request.raw_post_data
        req_text += '\nsession_key = %s' % request.session.session_key
        req_text += '\n******* META section *********'
        req_text += str(request.META)
        req_text += '\n******* COOKIES section *********'
        req_text += str(request.COOKIES)
        req_text += '\n******* POST section *********'
        req_text += str(request.POST)
        req_text += '\n******* GET section *********'
        req_text += str(request.GET)
        req_text += '\n******* REQUEST section *********'
        req_text += str(request.GET)
        req_text += '\n******* FILES section *********'
        req_text += str(request.GET)
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
        new_rec.is_secure = str(request.is_secure())
        new_rec.is_ajax = str(request.is_ajax())
        new_rec.save()

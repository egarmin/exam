# -*- coding: utf-8 -*-
from tddspry.django import HttpTestCase
from loginfo.models import LogRequest
from django.core.urlresolvers import reverse
from loginfo.views import display_requests

class MiddlewarePerson(HttpTestCase):
    '''  middleware ReqLog test '''

    def request_log_test(self):
        """ request record test   """

        self.client.get('/someurl1/')
        self.client.get('/someurl2/?somevariable1=somevalue1& \
                                    somevariable2=somevalue2')
        try:
            log = LogRequest.objects.order_by('-added')[0]
        except:
            self.assert_true(False)
        else:
            content = log.content
            self.assert_true('somevariable1=somevalue1' in content)
            self.assert_true('somevariable2=somevalue2' in content)
            self.assert_equal(log.path, '/someurl2/')


class TestDisplayRequest(HttpTestCase):
    """ Test main page with requests """

    def disp_req_test(self):
        for i in range(1, 11):
            response = self.get('/url_%s/?var%s=val%s' %(i, i, i))
        self.get200(reverse(display_requests))
        for i in range(1, 11):
            self.find('/url_%s/' % i )
            self.find('var%s=val%s' % (i, i) )


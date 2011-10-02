# -*- coding: utf-8 -*-
from tddspry.django import HttpTestCase
from loginfo.models import LogRequest


class MiddlewarePerson(HttpTestCase):
    '''  middleware ReqLog test '''

    def request_log_test(self):
        """ request record test   """

        self.client.get('/someurl1/')
        self.client.get('/someurl2/?somevariable1=somevalue1&somevariable2=somevalue2')
        try:
            log = LogRequest.objects.order_by('-added')[0]
        except:
            self.assert_true(False)
        else:
            content = log.content
            self.assert_true('somevariable1 = somevalue1' in content)
            self.assert_true('somevariable2 = somevalue2' in content)
            self.assert_equal(log.path, '/someurl2/')

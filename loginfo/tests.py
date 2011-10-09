# -*- coding: utf-8 -*-
from tddspry.django import HttpTestCase, DatabaseTestCase
from loginfo.models import LogRequest, LogModel
from personal.models import Person
from django.core.urlresolvers import reverse
from loginfo.views import display_requests


class MiddlewareRequest(HttpTestCase):
    '''  middleware ReqLog test '''

    def request_log_test(self):
        """ request record test   """

        self.client.get('/someurl1/')
        self.client.get('/someurl2/?somevariable1=somevalue1& \
                                    somevariable2=somevalue2')
        log = LogRequest.objects.order_by('-added')[0]
        content = log.content
        self.assert_true('somevariable1 = somevalue1' in content)
        self.assert_true('somevariable2 = somevalue2' in content)
        self.assert_equal(log.path, '/someurl2/')


class TestDisplayRequest(HttpTestCase):
    """ Test main page with requests """

    def disp_req_test(self):
        for i in range(1, 11):
            self.get('/url_%s/?var%s=val%s' % (i, i, i))
        self.get200(reverse(display_requests))
        for i in range(1, 11):
            self.find('/url_%s/' % i)
            self.find('var%s = val%s' % (i, i))

class TestLogModel(DatabaseTestCase):
    """  Log changing, creating and deleting of all models
    """

    def log_model_test(self):
        pers = Person(name='test_name', surname='test_surname')
        pers.save()
        last = LogModel.objects.order_by('-added')[0]
        self.assert_equal(last.app_name, 'personal')
        self.assert_equal(last.model_name, 'person')
        self.assert_equal(last.action, 'create')
        name = Person.objects.get(pk=last.id_obj).name
        self.assert_equal(name, 'test_name')

        pers = Person.objects.get(name='test_name')
        pers.name = 'new_user_name'
        pers.save()
        last = LogModel.objects.order_by('-added')[0]
        self.assert_equal(last.app_name, 'personal')
        self.assert_equal(last.model_name, 'person')
        self.assert_equal(last.action, 'change')
        name = Person.objects.get(pk=last.id_obj).name
        self.assert_equal(name, 'new_user_name')


        pers = Person.objects.get(name='new_user_name')
        pers.name = 'new_user_name'
        pers.delete()
        last = LogModel.objects.order_by('-added')[0]
        self.assert_equal(last.app_name, 'personal')
        self.assert_equal(last.model_name, 'person')
        self.assert_equal(last.action, 'delete')
        try:
            pers = Person.objects.get(pk=last.id_obj)
        except Person.DoesNotExist:
            pass


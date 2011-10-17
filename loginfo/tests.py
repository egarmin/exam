# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from time import sleep

from tddspry.django import HttpTestCase, DatabaseTestCase

from loginfo.models import LogRequest, LogModel
from loginfo.views import display_requests
from personal.models import Person


class MiddlewareRequest(HttpTestCase):
    """  middleware ReqLog test """

    def request_log_test(self):
        # request record test

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
    # create
    def log_model_test(self):
        pers = Person(name='test_name', surname='test_surname')
        pers.save()
        last = LogModel.objects.order_by('-added')[0]
        self.assert_equal(last.app_name, 'personal')
        self.assert_equal(last.model_name, 'person')
        self.assert_equal(last.action, 'create')
        name = Person.objects.get(pk=last.id_obj).name
        self.assert_equal(name, 'test_name')
        # change
        pers = Person.objects.get(name='test_name')
        pers.name = 'new_user_name'
        pers.save()
        last = LogModel.objects.order_by('-added')[0]
        self.assert_equal(last.app_name, 'personal')
        self.assert_equal(last.model_name, 'person')
        self.assert_equal(last.action, 'change')
        name = Person.objects.get(pk=last.id_obj).name
        self.assert_equal(name, 'new_user_name')
        # delete
        pers = Person.objects.get(name='new_user_name')
        pers.delete()
        last = LogModel.objects.order_by('-added')[0]
        self.assert_equal(last.app_name, 'personal')
        self.assert_equal(last.model_name, 'person')
        self.assert_equal(last.action, 'delete')
        pers_list = Person.objects.filter(pk=last.id_obj)
        self.assert_false(pers_list)


class PriorityTest(HttpTestCase):
    """ Test ordering logRequest """
    def prior_test(self):
        for i in range(0, 10):
            sleep(1.3)
            self.client.get('/someurl_%s/' % i)

        for i in range(1, 11):
            log = LogRequest.objects.get(pk=i)
            log.priority = 11 - i
            log.save()
        #order by priority field
        self.go('/middle/?field=priority')
        s = self.show()
        for i in range(0, 9):
            self.assert_true(s.find('id="prior">%s<' % (i + 1)) <
                             s.find('id="prior">%s<' % (i + 2)))
        #reverse order by priority field
        self.go('/middle/?field=priority')
        s = self.show()
        for i in range(0, 9):
            self.assert_true(s.find('id="prior">%s<' % (i + 1)) >
                             s.find('id="prior">%s<' % (i + 2)))

        #order by path field
        self.go('/middle/?field=path')
        s = self.show()
        for i in range(0, 9):
            self.assert_true(s.find('id="path">/someurl_%s/<' % i) <
                             s.find('id="path">/someurl_%s/<' % (i + 1)))
        #reverse order by path field
        self.go('/middle/?field=path')
        s = self.show()
        for i in range(0, 9):
            self.assert_true(s.find('id="path">/someurl_%s/<' % i) >
                             s.find('id="path">/someurl_%s/<' % (i + 1)))

        #order by pk field
        self.go('/middle/?field=pk')
        s = self.show()
        for i in range(0, 9):
            self.assert_true(s.find('pk = %s' % (i + 1)) <
                             s.find('pk = %s' % (i + 2)))

        #order by added field
        log = LogRequest.objects.all().order_by('added')
        self.go('/middle/?field=added')
        s = self.show()
        for i in range(0, 9):
            t1 = log[i].added.strftime('%H:%M:%S')
            t2 = log[i + 1].added.strftime('%H:%M:%S')
            self.assert_true(s.find('(%s)' % t1) <
                             s.find('(%s)' % t2))
        #reverse order by added field
        #log = LogRequest.objects.all().order_by('-added')
        self.go('/middle/?field=added')
        s = self.show()
        for i in range(0, 9):
            t1 = log[i].added.strftime('%H:%M:%S')
            t2 = log[i + 1].added.strftime('%H:%M:%S')
            self.assert_true(s.find('(%s)' % t1) >
                             s.find('(%s)' % t2))

        # order by pk field
        self.go('/middle/?field=pk')
        s = self.show()
        for i in range(0, 9):
            self.assert_true(s.find('pk = %s' % (i + 1)) <
                             s.find('pk = %s' % (i + 2)))

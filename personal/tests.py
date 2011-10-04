# -*- coding: utf-8 -*-
from tddspry.django import DatabaseTestCase, HttpTestCase
from personal.models import Person


NEW_NAME = 'newperson'
TEST_NAME = 'testperson'


class TestPerson(DatabaseTestCase):
    '''  CRUD test'''
    def create_test(self):
        self.assert_create(Person, name=TEST_NAME)

    def read_test(self):
        self.assert_create(Person, name=TEST_NAME)
        self.assert_read(Person, name=TEST_NAME)

    def update_test(self):
        person = self.assert_create(Person, name=TEST_NAME)
        self.assert_update(person, name=NEW_NAME)

    def delete_test(self):
        person = self.assert_create(Person, name=TEST_NAME)
        self.assert_delete(person)


class TestDisplayPerson(HttpTestCase):
    """ Test main page with pers-data. """

    def disp_pers_test(self):
        self.get200('/')
        self.find('Name')
        self.find('Surname')
        self.find('Date of birth')
        self.find('Biography')
<<<<<<< HEAD
        self.find('Phone')
        self.find('E-mail')


class TestContextProcessor(HttpTestCase):
    ''' Test adding SETTINGS to context '''

    def context_test(self):
        response = self.client.get('/')
        self.assert_true('settings' in response.context[0],
                         'No django.settings in context.')
=======
        self.find('Jabber')
        self.find('Skype')
        self.find('Email')
>>>>>>> t3_middle

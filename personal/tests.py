# -*- coding: utf-8 -*-
from tddspry.django import DatabaseTestCase, HttpTestCase
from personal.models import Person, Contacts
import settings
from django.utils import simplejson as json

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
        self.find('Jabber')
        self.find('Skype')
        self.find('Email')


class TestContextProcessor(HttpTestCase):
    ''' Test adding SETTINGS to context '''

    def context_test(self):
        response = self.client.get('/')
        self.assert_true('settings' in response.context[0],
                         'No django.settings in context.')


class TestContactEdit(HttpTestCase):
    """ Test contact edit form work """

    def contact_edit_test(self):
        #Prepare test data
        TEST_DATA = {'name': 'test_name',
                     'surname': 'test_surname',
                     'birthday': '01.01.2010',
                     'bio': 'test_bio',
                     'email': 'test@test.com',
                     'jid': 'test@jabb-jabb.puk',
                     'appendix': 'pizza',
                     'skype': 'my.name.is'
                     }
        #Login testuser
        self.helper('create_user', 'testuser', 'password')
        self.login('testuser', 'password')
        #Send post request to edit pers
        self.client.post('/edit/', TEST_DATA,
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        #Get edited pers
        pers = Person.objects.get(pk=1)
        cont = Contacts.objects.get(person=pers)

        #Compare pers members with test dict fields
        self.assert_equal(pers.name, TEST_DATA['name'])
        self.assert_equal(pers.surname, TEST_DATA['surname'])
        self.assert_equal(pers.birthday.strftime("%d.%m.%Y"),
                          TEST_DATA['birthday'])
        self.assert_equal(pers.bio, TEST_DATA['bio'])
        self.assert_equal(cont.email, TEST_DATA['email'])
        self.assert_equal(cont.jid, TEST_DATA['jid'])
        self.assert_equal(cont.skype, TEST_DATA['skype'])
        self.assert_equal(cont.appendix, TEST_DATA['appendix'])




class TestAuthPage(HttpTestCase):

    def test_login(self):
        self.helper('create_user', 'username', 'password')
        self.login('username', 'password')
        self.url(settings.LOGIN_REDIRECT_URL)

    def test_logout(self):
        self.helper('create_user', 'testuser', 'password')
        self.login('testuser', 'password')
        self.logout()
        self.url('/')


class TestAjaxValid(HttpTestCase):
    
    def ajax_messages_test(self):
        FAIL_TEST_DATA = {'name': u'',
                     'surname': u'',
                     'birthday': u'abcdef',
                     'email': u'fail_email',
                     'jid': u'123123'}
        self.helper('create_user', 'testuser', 'password')
        self.login('testuser', 'password')

        response = self.client.post('/edit/', FAIL_TEST_DATA,
                         HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        errors = json.loads(response.content)
        self.assert_equal(errors['pers_errors']['name'][0],
                            'Enter your name, please.')
        self.assert_equal(errors['pers_errors']['surname'][0],
                            'Enter your surname, please.')
        self.assert_equal(errors['pers_errors']['birthday'][0],
                           'Enter a valid date.')
        self.assert_equal(errors['cont_errors']['email'][0],
                            'Enter a valid e-mail address.')
        self.assert_equal(errors['cont_errors']['jid'][0],
                            'Enter a valid jabber ID.')



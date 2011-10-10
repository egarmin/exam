# -*- coding: utf-8 -*-
from tddspry.django import DatabaseTestCase, HttpTestCase, TestCase
from personal.models import Person
import settings
import commands
import sys
from os import path, unlink
from StringIO import StringIO
from django.core.management import call_command
from django.utils import simplejson as json
from django.template import Template, Context
from django.contrib.contenttypes.models import ContentType
from datetime import date


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

        #Compare pers members with test dict fields
         #Compare pers members with test dict fields
        self.assert_equal(pers.name, TEST_DATA['name'])
        self.assert_equal(pers.surname, TEST_DATA['surname'])
        self.assert_equal(pers.birthday.strftime("%d.%m.%Y"),
                          TEST_DATA['birthday'])
        self.assert_equal(pers.bio, TEST_DATA['bio'])
        self.assert_equal(pers.email, TEST_DATA['email'])
        self.assert_equal(pers.jid, TEST_DATA['jid'])
        self.assert_equal(pers.skype, TEST_DATA['skype'])
        self.assert_equal(pers.appendix, TEST_DATA['appendix'])


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


class TestReverse(HttpTestCase):

    def reverse_order_test(self):
        self.helper('create_user', 'testuser', 'password')
        self.login('testuser', 'password')
        self.go('/edit/')
        s = self.show()
        self.assert_true(s.find('Appendix') < s.find('Email'))
        self.assert_true(s.find('Email') < s.find('Skype'))
        self.assert_true(s.find('Skype') < s.find('Jabber'))
        self.assert_true(s.find('Biography') < s.find('Date of birth'))
        self.assert_true(s.find('Date of birth') < s.find('Surname'))
        self.assert_true(s.find('Surname') < s.find('Name'))


class TestAjaxValid(HttpTestCase):
    """ Via ajax """
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
        self.assert_equal(errors['pers_errors']['email'][0],
                            'Enter a valid e-mail address.')
        self.assert_equal(errors['pers_errors']['jid'][0],
                            'Enter a valid jabber ID.')


class TestAdminLink(TestCase):
    """ Test tag that renders the link to its admin edit page """

    def test_admin_link(self):
        # test for object
        pers = Person.objects.get(pk=1)
        pattern = "/admin/{app}/{module}/{obj_pk}/".\
                format(app=pers._meta.app_label,
                       module=pers._meta.module_name,
                       obj_pk=pers.pk)
        template = Template('{% load owntag %}{% admin_link contact %}')
        res = template.render(Context({'contact': pers}))
        self.assert_equal(res, pattern)


class TestCountModel(TestCase):
    """  Count model, dat-file
    """

    def test_count(self):
        ct = ContentType.objects.all()
        old_out = sys.stdout
        old_err = sys.stderr
        out_out = StringIO()
        out_err = StringIO()
        sys.stdout = out_out
        sys.stderr = out_err
        call_command('allmodels')
        sys.stdout = old_out
        sys.stderr = old_err
        for c in ct:
            self.find_in(c.model, out_out.getvalue().lower())
            self.find_in(c.model, out_err.getvalue().lower())
            self.find_in(c.app_label, out_out.getvalue().lower())
            self.find_in(c.app_label, out_err.getvalue().lower())
        self.find_in('error:', out_err.getvalue().lower())

    def test_script_file(self):
        filename = '/tmp/' + date.today().strftime('%Y-%m-%d') + '.dat'
        try:
            unlink(filename)
        except OSError:
            pass
        commands.getoutput('bashscript.sh')
        out = open(filename).read()
        ct = ContentType.objects.all()
        for c in ct:
            self.find_in(c.model, out.lower())
            self.find_in(c.app_label, out.lower())
        self.find_in('error:', out)

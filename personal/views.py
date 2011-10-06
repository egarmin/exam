# -*- coding: utf-8 -*-
from personal.models import Person, Contacts
from personal.forms import PersonForm, ContactForm
from django.utils.translation import ugettext_lazy as _
from personal.decorators import render_to
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.utils import simplejson as json
from django.template import loader, RequestContext


@render_to('display_pers.html')
def display_person(request):
    try:
        pers = Person.objects.get(pk=1)
    except:
        pers = None
    contlist = Contacts.objects.filter(person=pers)
    return {'pers': pers, 'contlist': contlist}


@login_required
def edit_person(request):
    try:
        pers = Person.objects.get(pk=1)
    except:
        pers = None
    cont = pers.contacts.all()[0]
    if request.method == 'POST':
        ajax = request.is_ajax() #
        c_form_set = formset_factory(Contacts, formset=ContactForm)
        p_form = PersonForm(request.POST)
        c_form = c_form_set(request.POST)
        is_c_valid = c_form.is_valid()
        if p_form.is_valid() and is_c_valid:# forms are correct
            data = p_form.cleaned_data
            pers.name = data['name']
            pers.surname = data['surname']
            pers.birthday = data['birthday']
            pers.bio = data['bio']
            data = c_form.cleaned_data
            cont.jid = data['jid']
            cont.skype = data['skype']
            cont.appendix = data['appendix']
            cont.email = data['email']
            pers.save()
            cont.save()
            out = {'status': 'ok'}
        else:
            out = {'status': 'FAIL',
                   'pers_errors': p_form.errors,
                   'cont_errors': c_form.errors}
        if ajax:
            return HttpResponse(json.dumps(out), mimetype='application/json')
    else:
        p_form = PersonForm({'name': pers.name,
                           'surname': pers.surname,
                           'bio': pers.bio,
                           'birthday': pers.birthday
                           })
        c_form = ContactForm({'jid': cont.jid,
                             'skype': cont.skype,
                             'appendix': cont.appendix,
                             'email': cont.email
                           })
        tm = loader.get_template('edit_pers.html')
        c = RequestContext(request, {'person_form': p_form, 'contact_form': c_form})
        return HttpResponse(tm.render(c))

# -*- coding: utf-8 -*-
from personal.models import Person, Contacts
from personal.forms import PersonForm, ContactForm
from django.utils.translation import ugettext_lazy as _
from personal.decorators import render_to
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.utils import simplejson as json

@render_to('display_pers.html')
def display_person(request):
    try:
        pers = Person.objects.get(pk=1)
        cont = Contacts.objects.get(pk=1)
    except:
        pers = None
        cont = None
    return {'pers': pers, 'cont': cont}


@login_required
def edit_person(request):
    if request.method == 'POST':
        try:
            pers = Person.objects.get(pk=1)
            cont = Contacts.objects.get(person=pers)
        except:
            return HttpResponse('DB error')
        c_form_set = formset_factory(Contacts, formset=ContactForm)
        p_form = PersonForm(request.POST)
        c_form = c_form_set(request.POST)
        if p_form.is_valid() and c_form.is_valid():
            try:
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
            except:
                p_form.profilesave_error = _('Pers save error. Try later.')
                c_form.profilesave_error = _('Cont save error. Try later.')
            out = {}
        else:
            out_f = dict()
            out_f['p'] = p_form.errors
            out_f['c'] = c_form.errors
            out = json.dumps(out_f)
        return HttpResponse(out, mimetype='application/json')
    return HttpResponse({})



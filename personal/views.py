# -*- coding: utf-8 -*-
from personal.models import Person, Contacts
from personal.forms import PersonForm, ContactForm
from django.utils.translation import ugettext_lazy as _
from personal.decorators import render_to
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory


@render_to('display_pers.html')
def display_person(request):
    try:
        pers = Person.objects.get(pk=1)
        cont = Contacts.objects.filter(person=pers)
    except:
        pers = None
        cont = None
    return {'pers': pers, 'cont': cont}


@login_required
@render_to('edit_pers.html')
def edit_person(request):
    try:
        pers = Person.objects.get(pk=1)
        cont = Contacts.objects.filter(person=pers)
    except:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
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
    return {'person_form': p_form, 'contact_form': c_form}

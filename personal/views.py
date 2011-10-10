# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from personal.decorators import render_to
from personal.forms import PersonForm
from personal.models import Person


@render_to('display_pers.html')
def display_person(request):
    try:
        pers = Person.objects.get(pk=1)
    except Person.DoesNotExist:
        pers = None
    return {'pers': pers}


@login_required
@render_to('edit_pers.html')
def edit_person(request):
    index = 4
    try:
        pers = Person.objects.get(pk=1)
    except Person.DoesNotExist:
        pers = None
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        p_form = PersonForm(request.POST)
        if p_form.is_valid():
            data = p_form.cleaned_data
            pers.name = data['name']
            pers.surname = data['surname']
            pers.birthday = data['birthday']
            pers.bio = data['bio']
            pers.jid = data['jid']
            pers.skype = data['skype']
            pers.appendix = data['appendix']
            pers.email = data['email']
            pers.save()
    else:
        p_form = PersonForm({'name': pers.name,
                            'surname': pers.surname,
                            'bio': pers.bio,
                            'birthday': pers.birthday,
                            'jid': pers.jid,
                            'skype': pers.skype,
                            'appendix': pers.appendix,
                            'email': pers.email
                           })
    return {'person_form': p_form, 'index': index}

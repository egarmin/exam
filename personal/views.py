# -*- coding: utf-8 -*-
from personal.models import Person
from personal.forms import PersonForm
from django.utils.translation import ugettext_lazy as _
from personal.decorators import render_to
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@render_to('display_pers.html')
def display_person(request):
    try:
        pers = Person.objects.get(pk=1)
    except:
        pers = None
    return {'pers': pers}


@login_required
@render_to('edit_pers.html')
def edit_person(request):
    try:
        pers = Person.objects.get(pk=1)
    except:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                pers.name = data['name']
                pers.surname = data['surname']
                pers.bio = data['bio']
                pers.birthday = data['birthday']
                pers.phone = data['phone']
                pers.email = data['email']
                pers.save()
            except:
                form.profilesave_error = _('Pers info save error. Try later.')
    else:
        form = PersonForm({'name': pers.name,
                           'surname': pers.surname,
                           'bio': pers.bio,
                           'birthday': pers.birthday,
                           'phone': pers.phone,
                           'email': pers.email
                           })
    return {'form':form}

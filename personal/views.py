# -*- coding: utf-8 -*-
from personal.models import Person
from personal.forms import PersonForm
from personal.decorators import render_to
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import simplejson as json
from django.template import RequestContext
from django.shortcuts import render_to_response


@render_to('display_pers.html')
def display_person(request):
    try:
        pers = Person.objects.get(pk=1)
    except Person.DoesNotExist:
        pers = None
    return {'pers': pers}


@login_required
def edit_person(request):
    index = 4
    try:
        pers = Person.objects.get(pk=1)
    except Person.DoesNotExist:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        p_form = PersonForm(request.POST)
        if p_form.is_valid():  # forms are correct
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
            if request.is_ajax():
                out = {'status': 'ok'}
                return HttpResponse(json.dumps(out), mimetype='application/json')
            return render_to_response('edit_pers.html',
                              {'person_form': p_form, 'index': index},
                              context_instance=RequestContext(request))
        else:
            out = {'status': 'FAIL',
                   'pers_errors': p_form.errors}
            if request.is_ajax():
                return HttpResponse(json.dumps(out), mimetype='application/json')
            return render_to_response('edit_pers.html',
                              {'person_form': p_form, 'index': index},
                              context_instance=RequestContext(request))
            #return HttpResponseRedirect('/edit/')
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
        return render_to_response('edit_pers.html',
                              {'person_form': p_form, 'index': index},
                              context_instance=RequestContext(request))

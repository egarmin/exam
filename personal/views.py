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

@render_to('edit_pers.html')
@login_required
def edit_person(request):
    index = len(PersonForm.base_fields.keyOrder) / 2
    try:
        pers = Person.objects.get(pk=1)
    except Person.DoesNotExist:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        p_form = PersonForm(instance=pers, data=request.POST)
        if p_form.is_valid():  # forms are correct
            p_form.save()
            out = {'status': 'ok'}
        else:
            out = {'status': 'fail',
                   'pers_errors': p_form.errors}
        if request.is_ajax():
                return HttpResponse(json.dumps(out),
                                    mimetype='application/json')
        return {'person_form': p_form, 'index': index}
    else:
        p_form = PersonForm(instance=pers)
        return {'person_form': p_form, 'index': index}

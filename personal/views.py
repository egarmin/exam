# -*- coding: utf-8 -*-

from personal.models import Person
from personal.decorators import render_to
from django.http import HttpResponse

@render_to('display_pers.html')
def display_person(request):
    return HttpResponse('test')

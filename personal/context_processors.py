from django.conf import settings


def addsettings (request):
    return {'settings': settings}

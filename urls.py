# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.defaults import url, patterns, include


from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('personal.urls')),
    url(r'^media/(.*)$', 'django.views.static.serve',
        kwargs={'document_root': settings.MEDIA_ROOT}),

)

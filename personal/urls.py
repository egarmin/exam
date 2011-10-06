from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('personal.views',
    url(r'^$', 'display_person'),
    url(r'^edit/$', 'edit_person'),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login',
        {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'logout', {'next_page': '/'}),
)

#For calendar widget
urlpatterns += patterns('',
    (r'^jsi18n/', 'django.views.i18n.javascript_catalog'),
)
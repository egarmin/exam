from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('loginfo.views',
    url(r'^middle/$', 'display_requests'),
)

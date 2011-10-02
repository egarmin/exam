from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('personal.views',
    url(r'^$', 'display_person'),
)
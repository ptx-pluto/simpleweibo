from django.conf.urls import patterns, include, url

urlpatterns = patterns('mysite.views',
#    url(r'^$'     , 'index_view'),
#    url(r'^index$', 'index_view'),

    url(r'^account/login$'   , 'login_view'),
    url(r'^account/register$', 'register_view'),

#    url(r'^feed/timeline$', 'timeline_view'),
    url(r'^feed/myfeed$'  , 'myfeed_view'),
#    url(r'^feed/archive$' , 'archive_view'),
)

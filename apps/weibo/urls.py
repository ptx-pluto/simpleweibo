
from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'weibo.views',

#    url(r'^account/bind$' , 'bind_account'),
    url(r'^stream/home$'   , 'home_stream'),
    url(r'^stream/archive$', 'archive_stream'),
    url(r'^stream/root$'   , 'timeline_stream'),
    url(r'^stream/profile/(?P<profile>\d{10})$', 'profile_stream'),
)


from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'weibo.views',

#    url(r'^account/bind$' , 'bind_account'),
    url(r'^stream/home$'   , 'stream_view', { 'name': 'home' }),
    url(r'^stream/archive$', 'stream_view', { 'name': 'archive' }),
    url(r'^stream/root$'   , 'stream_view', { 'name': 'root' }),
    url(r'^stream/profile/(?P<uid>\d+)$', 'stream_view', { 'name': 'profile' }),
)

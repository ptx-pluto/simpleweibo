from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'weibo.views',
    url(r'^account/bind$' , 'bind_account'),
    url(r'^account/token$', 'fetch_token'),

    url(r'^feed/timeline$' , 'timeline_feed'),
    url(r'^feed/following$', 'following_feed'),
    url(r'^feed/archive$'  , 'archive_feed'),

#    url(r'^oauth/login$', 'login_request'),
#    url(r'^oauth/token$', 'get_sina_code'),

)

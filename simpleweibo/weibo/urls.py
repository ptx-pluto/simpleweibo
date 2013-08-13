from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'simpleweibo.weibo.views',
    url(r'^$', 'weibo_index'),
    url(r'^index$', 'weibo_index'),

    url(r'^home$',           'home_timeline'),
    url(r'^home/timeline$',  'home_timeline'),
    url(r'^home/archive$',   'home_archive'),
    url(r'^home/follower$',  'home_follower'),
    url(r'^home/following$', 'home_following'),
    
    url(r'^search/$',                'search_view'),
    url(r'^search/(?P<domain>\S+)$', 'search_view'),

#    url(r'^oauth/login$', 'login_request'),
#    url(r'^oauth/token$', 'get_sina_code'),

    url(r'^test/init$', 'weibo_init'),
    url(r'^test/clear$', 'weibo_clear'),
    url(r'^test/$', 'test'),

)

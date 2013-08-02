from django.conf.urls import patterns, include, url

urlpatterns = patterns('simpleweibo.weibo.views',
    url(r'^$', 'weibo_index'),
    url(r'^index$', 'weibo_index'),

    url(r'^home$',           'home_timeline'),
    url(r'^home/timeline$',  'home_timeline'),
    url(r'^home/archive$',   'home_archive'),
    url(r'^home/follower$',  'home_follower'),
    url(r'^home/following$', 'home_following'),

    url(r'^search/$',              'search_all_feed'),
    url(r'^search/all-feed$',      'search_all_feed'),
    url(r'^search/my-feed$',       'search_my_feed'),
    url(r'^search/home-timeline$', 'search_home_timeline'),
    url(r'^search/archive$',       'search_archive'),


#    url(r'^oauth/login$', 'login_request'),
#    url(r'^oauth/token$', 'get_sina_code'),

    url(r'^test/init$', 'weibo_init'),
    url(r'^test/clear$', 'weibo_clear'),
    url(r'^test/$', 'test'),

)

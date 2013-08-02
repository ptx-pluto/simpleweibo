from django.conf.urls import patterns, include, url

from simpleweibo.weibo.models import Profile
from simpleweibo.weibo.views import ProfileList, FollowerList, FollowingList, FriendList

urlpatterns = patterns('simpleweibo.weibo.views',
    url(r'^home$', 'weibo_home'),
    url(r'^index$', 'weibo_index'),

    url(r'^search/$', 'weibo_search_allfeed'),
    url(r'^search/allfeed$', 'weibo_search_allfeed'),
    url(r'^search/mytimeline$', 'weibo_search_mytimeline'),
    url(r'^search/hometimeline$', 'weibo_search_hometimeline'),
    url(r'^search/archive$', 'weibo_search_archive'),

    url(r'^timeline$', 'weibo_timeline'),

    url(r'^ajax/friend$', FriendList.as_view()),
    url(r'^ajax/follower$', FollowerList.as_view()),
    url(r'^ajax/following$', FollowingList.as_view()),
    url(r'^ajax/profile$', ProfileList.as_view()),
    url(r'^ajax/profile.json$', 'profile_json'),

#    url(r'^oauth/login$', 'login_request'),
#    url(r'^oauth/token$', 'get_sina_code'),

    url(r'^test/init$', 'weibo_init'),
    url(r'^test/clear$', 'weibo_clear'),
    url(r'^test/$', 'test'),

)

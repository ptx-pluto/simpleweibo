import json

from django.contrib.auth.decorators import login_required

from account.models import UserAccount
from weibo.models import WeiboBinding, Feed, Profile 
from view_decorators import rest_api

LOGIN_URL = '/profile/login'

#==========================================
# /profile/following
# /profile/settings
#==========================================

@login_required
@rest_api
def following_list(request):
    user_account = request.user.account
    if request.method == 'GET':
        return [json.dumps(p.content) for p in user_account.binding.following]


# @login_required
# @rest_api
# def weibo_binding(request):
#     user_account = request.user.account
#     if request.method == 'GET':
#         try:
#             binding = WeiboBinding.objects.get()
#         except WeiboBinding.DoesNotExist:
#             binding = None
#     elif request.method == 'PUT':
#             binding, is_new = WeiboBinding.objects.get_or_create()


#==========================================
# /stream/profile/:id
# /stream/root
# /stream/home
# /stream/archive
#==========================================

@login_required
@rest_api
def stream_view(request, name='root'):
    if request.method == 'GET':
        if name == 'home':
            stream = request.user.account.binding.bind_profile.timeline
        elif name == 'archive':
            stream = request.user.account.binding.archive
        elif name == 'profile':
            stream = Profile.objects.get(uid=uid).timeline
        else:
            stream = request.user.account.binding.bind_profile.timeline

        assert not ('head' in request.GET and 'tail' in request.GET)
            
        if 'head' in request.GET:
            feed_set = timeline.filter(feed_id__gt=request.GET['head']).order_by('feed_id').reverse()
        elif 'tail' in request.GET:
            feed_set = timeline.filter(feed_id__lt=request.GET['tail']).order_by('feed_id').reverse()[0:40]
        else:
            feed_set = timeline.order_by('feed_id').reverse()[0:40]

        return [json.loads(feed.content) for feed in feed_set]


# @login_required
# @rest_api
# def stream_view(request, stream):
#     if request.method == 'GET':
#         pass
#     elif request.method == 'POST':
#         pass
#     elif request.method == 'PUT':
#         pass
#     elif request.method == 'PATCH':
#         pass
#     elif request.method == 'DELETE':
#         pass

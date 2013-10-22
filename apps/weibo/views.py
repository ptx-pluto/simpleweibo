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
def home_stream(request):
    user_account = request.user.account
    if request.method == 'GET':
        feed_set = user_account.binding.bind_profile.timeline.order_by('create_time').reverse()[0:40]
        return [json.loads(feed.content) for feed in feed_set]


@login_required
@rest_api
def root_stream(request):
    user_account = request.user.account
    if request.method == 'GET':
        feed_set = user_account.binding.bind_profile.timeline.order_by('create_time').reverse()[0:40]
        return [json.loads(feed.content) for feed in feed_set]


@login_required
@rest_api
def archive_stream(request):
    user_account = request.user.account
    if request.method == 'GET':
        feed_set = user_account.binding.bind_profile.timeline.order_by('create_time').reverse()[0:40]
        return [json.loads(feed.content) for feed in feed_set]


@login_required
@rest_api
def profile_stream(request):
    if request.method == 'GET':
        feed_set = Profile.objects.get(uid=profile).timeline.order_by('create_time').reverse()[0:40]
        return [json.loads(feed.content) for feed in feed_set]


@login_required
@rest_api
def stream_view(request, stream):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'PATCH':
        pass
    elif request.method == 'DELETE':
        pass

import os
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from weibowrapper.shortcuts import *
from weibo.models import Feed, Profile, WeiboBinding

#=====================================================================================

LOGIN_URL = '/account/login'

def login_view(request):
    return render_to_response('root/account/login.html',{})


def register_view(request):
    return render_to_response('root/account/register.html',{})


@login_required()
def myfeed_view(request):
    feed_set = request.user.account.binding.bind_profile.timeline.all().order_by('create_time').reverse()[0:40]
    feeds = [json.loads(feed.content) for feed in feed_set]
    return render_to_response('root/feed/myfeed.html', {'feed_list': feeds})

# @login_view(LOGIN_URL)
# def timeline_view(request):
#     feed_set = request.user.account.binding.bind_profile.timeline.all()[0:40]
#     feeds = [json.loads(feed.content) for feed in feed_set]
#     return render_to_response('root/feed/myfeed.html', feed_list=feeds)


# @login_view(LOGIN_URL)
# def archive_view(request):
#     feed_set = request.user.account.binding.bind_profile.timeline.all()[0:40]
#     feeds = [json.loads(feed.content) for feed in feed_set]
#     return render_to_response('root/feed/myfeed.html', feed_list=feeds)

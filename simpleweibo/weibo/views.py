from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import ListView
import os, urllib, json

from weibowrapper.shortcuts import get_all_follower, get_all_following, get_all_myfeed
from simpleweibo.weibo.models import Profile

#=====================================================================================

def weibo_index(request):
    return render_to_response('index.html', {'feed_list': get_all_myfeed(None, source='json')})

#=====================================================================================

class ProfileList(ListView):
    model = Profile
    template_name = 'ajax-profile.html'

class FollowerList(ListView):
    queryset = Profile.objects.filter(follower=True)
    template_name = 'ajax-profile.html'

class FollowingList(ListView):
    queryset = Profile.objects.filter(following=True)
    template_name = 'ajax-profile.html'

class FriendList(ListView):
    queryset = Profile.objects.filter(follower=True, following=True)
    template_name = 'ajax-profile.html'

#=====================================================================================

#def login_request(request):
#    return render_to_response('login.html', {'AuthURL': sdk.get_oauth_uri()})

#def get_sina_code(request):
#    code = request.GET.get('code')
#    access_token = sdk.get_oauth_token(code)
#    return HttpResponse('')

#=====================================================================================

def profile_init(request):
    for profile in get_all_following(None, source='json'):
        p = Profile(uid=profile['id'], name=profile['name'], following=True, gender=profile['gender'])
        p.save()
    for profile in get_all_follower(None, source='json'):
        try:
            p = Profile.objects.get(uid=profile['id'])
            p.follower = True
        except:
            p = Profile(uid=profile['id'], name=profile['name'], follower=True, gender=profile['gender'])
        finally:
            p.save()
    return HttpResponse('Successed!')

def profile_clear(request):
    Profile.objects.all().delete()
    return HttpResponse('Successed!')


#=====================================================================================

def test(request):
    print(Profile.objects.get(uid='12345'))
    return 'Successed'

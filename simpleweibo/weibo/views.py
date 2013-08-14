import os, urllib, json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import ListView

from weibowrapper.shortcuts import *
from simpleweibo.weibo.models import Profile

#=====================================================================================

def weibo_index(request):
    return render_to_response('entrance/index.html', {'feed_list': get_all_myfeed(None, source='json')})

#=====================================================================================
# Weibo Home Views
#=====================================================================================

def home_timeline(request):
    return render_to_response('entrance/home/timeline.html', 
                              {'feed_list': get_all_myfeed(None, source='json')})

def home_archive(request):
    return render_to_response('entrance/home/archive.html', 
                              {'feed_list': get_all_archive(None, source='json')})

def home_follower(request):
    return render_to_response('entrance/home/follower.html', 
                              {'profile_list': get_all_follower(None, source='json')})

def home_following(request):
    return render_to_response('entrance/home/following.html',
                              {'profile_list': get_all_following(None, source='json')})

#=====================================================================================
# Weibo Search
#=====================================================================================

search_templates = {
    'all-feed': 'entrance/search/all-feed.html',
    'my-feed': 'entrance/search/my-feed.html',
    'home-timeline': 'entrance/search/home-timeline.html',
    'archive': 'entrance/search/archive.html',
}

search_domains = [
    'all-feed',
    'my-feed',
    'home-timeline',
    'archive',
]

def search_view(request, domain='all-feed'):
    assert domain in search_domains
    keyword = request.GET.get('search', request.COOKIES.get('LAST_SEARCH',''))
    results = search_weibo(keyword, domain=domain) if keyword != '' else []
    resp = render_to_response(search_templates[domain], {'result_list': results})
    resp.set_cookie('LAST_SEARCH', keyword)
    return resp

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

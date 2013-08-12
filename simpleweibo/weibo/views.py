from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import ListView
import os, urllib, json

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
# Weibo Search Views
#=====================================================================================

def search_enter(request):
    keyword = request.GET.get('search')
    if keyword and keyword != '':
        results = search_all(request.GET.get('search'))
    else:
        results = []
        keyword = ''
    resp = render_to_response('entrance/search/all-feed.html', {'result_list': results})
    resp.set_cookie('LAST_SEARCH', keyword)
    return resp

def search_all_feed(request):
    keyword = request.GET.get('search')
    if not keyword:
        if 'LAST_SEARCH' in request.COOKIES:
            keyword = request.COOKIES['LAST_SEARCH']
        else:
            keyword = ''
    if keyword != '':
        results = search_all(keyword)
    else:
        results = []
    resp = render_to_response('entrance/search/all-feed.html', {'result_list': results})
    resp.set_cookie('LAST_SEARCH', keyword)
    return resp

def search_my_feed(request):
    keyword = request.GET.get('search')
    if not keyword:
        if 'LAST_SEARCH' in request.COOKIES:
            keyword = request.COOKIES['LAST_SEARCH']
        else:
            keyword = ''
    if keyword != '':
        results = search_myfeed(keyword)
    else:
        results = []
    resp = render_to_response('entrance/search/my-feed.html', {'result_list': results})
    resp.set_cookie('LAST_SEARCH', keyword)
    return resp

def search_home_timeline(request):
    keyword = request.GET.get('search')
    if not keyword:
        if 'LAST_SEARCH' in request.COOKIES:
            keyword = request.COOKIES['LAST_SEARCH']
        else:
            keyword = ''
    if keyword != '':
        results = search_db(keyword)
    else:
        results = []
    resp = render_to_response('entrance/search/home-timeline.html', {'result_list': results})
    resp.set_cookie('LAST_SEARCH', keyword)
    return resp

def search_archive(request):
    keyword = request.GET.get('search')
    if not keyword:
        if 'LAST_SEARCH' in request.COOKIES:
            keyword = request.COOKIES['LAST_SEARCH']
        else:
            keyword = ''
    if keyword != '':
        results = search_my_archive(keyword)
    else:
        results = []
    resp = render_to_response('entrance/search/archive.html', {'result_list': results})
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

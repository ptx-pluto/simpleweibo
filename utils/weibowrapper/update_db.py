#!/usr/bin/env python
#=============================================================================================

import sys
import os
from datetime import datetime
from os.path import dirname, abspath, join

# Setup testing environment
PATH_UTILS = dirname(dirname(abspath(__file__)))
PATH_ROOT  = dirname(PATH_UTILS)
PATH_APPS  = join(PATH_ROOT, 'apps')
sys.path.append(PATH_ROOT)
sys.path.append(PATH_APPS)
sys.path.append(PATH_UTILS)
os.environ['DJANGO_SETTINGS_MODULE'] = 'simpleweibo.settings'

from weibowrapper import conf
from weibowrapper.shortcuts import *
from weibowrapper.sdk import WeiboAccount
from weibo.models import WeiboBinding, Profile, Feed
from account.models import UserAccount

#=============================================================================================

def store_profile(profile):
    p, is_new = Profile.objects.get_or_create(
        uid = str(profile['id']),
        defaults = { 'content': json.dumps(profile) }
    )    
    if not is_new:
        p.content = json.dumps(profile)
    return p


def store_feed(feed):
    if feed.get('deleted', '') == '1':
        print('deleted feed found')
        return None
        
    create_time = datetime.strptime(feed['created_at'], '%a %b %d %X %z %Y')
    source = store_profile(feed['user'])
    f, is_new = Feed.objects.get_or_create(
        feed_id = str(feed['id']), 
        defaults = { 'content': json.dumps(feed), 'source': source, 'create_time': create_time }
    )
    return f


def fetch_myfeed(account):
    for feed in get_all_myfeed(account):
        store_feed(feed)


def fetch_archive(account, binding):
    binding.archive.clear()
    for feed in get_all_archive(account):
        archived = store_feed(feed)
        binding.archive.add(archived)


def fetch_following(account, binding):
    binding.following.clear()
    for profile in get_following(account):
        following = store_profile(profile)
        binding.following.add(following)    


def fetch_my_info(account, binding):
    fetch_myfeed(account)
    fetch_following(account, bindind)
    fetch_archive(account, binding)
    store_profile(get_my_profile(account))


def fetch_timeline(account):
    for feed in get_all_timeline(account):
        store_feed(feed)


def partial_update():
    for binding in WeiboBinding.objects.all():
        account = binding.get_account()
        fetch_my_info(account, binding)


#=============================================================================================

if __name__ == '__main__':
    pass


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

def store_feed(feed):
    # filter out invalid feeds
    if feed.get('deleted', '') == '1':
        print('deleted feed found')
        return None
        
    uid = str(feed['user']['id'])
    create_time = datetime.strptime(feed['created_at'], '%a %b %d %X %z %Y')
    source, profile_is_new = Profile.objects.get_or_create(uid=uid, defaults={'content': json.dumps(feed['user'])})
    feed, feed_is_new = Feed.objects.get_or_create(feed_id=str(feed['id']), defaults={'content': json.dumps(feed), 'source': source, 'create_time': create_time})
    return feed

def fetch_myfeed(weibo_account):
    for feed in get_all_myfeed(weibo_account):
        store_feed(feed)

def fetch_archive(weibo_account):
    for feed in get_all_archive(weibo_account):
        store_feed(feed)

def fetch_timeline(weibo_account):
    for feed in get_all_timeline(weibo_account):
        store_feed(feed)

def partial_update():
    for binding in WeiboBinding.objects.all():
        account = binding.get_account()
        fetch_myfeed(account)
        fetch_archive(account)


#=============================================================================================

if __name__ == '__main__':
    pass


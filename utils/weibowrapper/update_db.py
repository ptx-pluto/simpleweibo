#!/usr/bin/env python
#=============================================================================================

import sys
import os
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
    if feed.get('deleted', '') == '1':
        return None
    source, is_new = Profile.objects.get_or_create(uid=str(feed['user']['id']),  
                                                   defaults={'content': json.dumps(feed['user'])})
    return Feed.objects.get_or_create(feed_id=str(feed['id']),
                                      defaults={'content': json.dumps(feed), 'source': source})

def fetch_myfeed(weibo_account):
    for feed in get_all_myfeed(weibo_account):
       try:
           store_feed(feed)
       except:
           print(feed)

def fetch_archive(weibo_account):
    for feed in get_all_archive(weibo_account):
       try:
           store_feed(feed)
       except:
           print(feed)

def fetch_timeline(weibo_account):
    for feed in get_all_timeline(weibo_account):
       try:
           store_feed(feed)
       except:
           print(feed)

def update_all_user():
    for binding in WeiboBinding.objects.all():
        fetch_myfeed(binding.get_account())


#=============================================================================================

if __name__ == '__main__':
    pass


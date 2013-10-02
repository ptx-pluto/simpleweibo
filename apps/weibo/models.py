import json

from django.db import models

from profile.models import UserAccount
from weibowrapper.sdk import WeiboAccount
from weibowrapper.shortcuts import get_all_timeline, get_all_archive, get_following, get_all_myfeed

#===============================================================================================

UID_LENGTH = 10
FEED_ID_LENGTH = 16

#===============================================================================================

class Profile(models.Model):
    uid = models.CharField(max_length=UID_LENGTH, primary_key=True)
    content = models.TextField()
    # Profile.timeline from Feed foreign key

class WeiboBinding(models.Model):
    bind_user = models.OneToOneField(UserAccount)
    bind_profile = models.OneToOneField(Profile)
    token = models.TextField()
    feed_head = models.CharField()
    following = models.ManyToManyField(Profile, null=True)    
    archive = models.ManyToManyField(Feed, null=True)

    def get_account(self):
        return WeiboAccount(self.bind_profile.uid, token=self.token)

    def fetch_archive(self):
        self.archive.clear()
        for feed in get_all_archive(self.get_account()):
            try:
                stored_feed = Feed.objects.get(feed_id=str(feed['id']))
            except Feed.DoesNotExist:
                stored_feed = store_feed(feed)
            self.archive.add(store_feed)

    def fetch_myfeed(self):
        for feed in get_all_myfeed(self.get_account()):
            store_feed(feed)

    def fetch_timeline(self):
        for feed in get_all_timeline(self.get_account()):
            store_feed(feed)
            
    def fetch_following(self):
        self.following.clear()
        for profile in get_following(self.get_account()):
            Profile.objects.create(uid=str(profile['id']), content=json.dumps(profile))

class Feed(models.Model):
    feed_id = models.CharField(max_length=FEED_ID_LENGTH, primary_key=True)
    content = models.TextField()
    source = models.ForeignKey(Profile, related_name='timeline')
    
#===============================================================================================

def store_feed(feed):
    uid = str(feed['user']['id'])
    try:
        source = Profile.objects.get(uid=uid)
    except Profile.DoesNotExist:
        source = Profile.objects.create(uid=uid, content=json.dumps(feed['user']))
    return Feed.objects.create(feed_id=str(feed['id']), content=json.dumps(feed), source=source)

import json
from django.db import models

from weibowrapper.sdk import WeiboAccount
from account.models import UserAccount

#==========================

UID_LENGTH = 10
FEED_ID_LENGTH = 16

#==========================

class Profile(models.Model):
    uid = models.CharField(max_length=UID_LENGTH, primary_key=True)
    content = models.TextField(null=True)

class Feed(models.Model):
    feed_id = models.CharField(max_length=FEED_ID_LENGTH, primary_key=True)
    create_time = models.DateTimeField()
    source = models.ForeignKey(Profile, related_name='timeline')
    content = models.TextField()

class WeiboBinding(models.Model):
    bind_account = models.OneToOneField(UserAccount, related_name='binding')
    bind_profile = models.OneToOneField(Profile, related_name='binding')
    token = models.TextField()
    following = models.ManyToManyField(Profile, related_name='follower',null=True)    
    archive = models.ManyToManyField(Feed, null=True)

    def get_account(self):
        return WeiboAccount(self.bind_profile.uid, token=self.token)


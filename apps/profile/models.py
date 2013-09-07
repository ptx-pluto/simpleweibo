from django.db import models
from django.contrib.auth.models import User

from weibowrapper.sdk import WeiboAccount
from apps.weibo.models import WeiboProfile

#=================================================================================================

class WeiboBinding(models.Model):
    user      = models.ForeignKey(User)
    profile   = models.ForeignKey(WeiboProfile, related_name='profile')
    token     = models.TextField()
    following = models.ManyToManyField(WeiboProfile, related_name='following')

    def weibo_account(self):
        return WeiboAccount(self.profile.uid, token=self.access_token)

    def __str__(self):
        return self.user.username

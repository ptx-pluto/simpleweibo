from django.db import models

class WeiboProfile(models.Model):
    uid = models.CharField(max_length=10, primary_key=True)
    profile_content = models.CharField()

    def __unicode__(self):
        return self.name

class Relation(models.Model):
    follower  = models.ForeignKey(WeiboProfile)
    following = models.ForeignKey(WeiboProfile)

    def __unicode__(self):
        return '%s is following %s' % (self.follower, self.following)


class Status(models.Model):
    status_id = models.CharField(primary_key=True)
    source_uid = models.CharField(max_length=10)
    retweet_id = models.CharField()
    status_content = models.CharField()

    def __unicode__(self):
        return self.status_id

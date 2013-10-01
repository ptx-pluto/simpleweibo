from django.db import models

UID_LENGTH = 1
FEED_ID_LENGTH = 1

class Profile(models.Model):
    uid = models.CharField()
    

class Account(models.Model):
    feed = models.OneToOneField(Profile)
    token = models.TextField()
    feed_head = models.CharField()

class Feed(models.Model):
    content = models.TextField()
    feed_id = models.CharField()
    time = models.DateTimeField()
    source = models.ForeignKey(Profile)



from django.db import models


class WeiboProfile(models.Model):
    uid = models.CharField(max_length=10, primary_key=True)
    content = models.TextField()
    
    def __str__(self):
        return self.uid

class Status(models.Model):
    status_id = models.CharField(max_length=11, primary_key=True)
    source_uid = models.ForeignKey(WeiboProfile)
    retweet_id = models.CharField(max_length=11)
    status_content = models.TextField()

    def __str__(self):
        return self.status_id

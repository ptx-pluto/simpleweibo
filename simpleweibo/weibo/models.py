from django.db import models

GENDER_CHOICE = (('m','Male'),
                 ('f','Female'),)

class Profile(models.Model):

    uid = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    following = models.BooleanField(default=False)
    follower = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

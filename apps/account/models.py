from django.db import models
from django.contrib.auth.models import User

#=================================================================================================

class UserAccount(models.Model):
    user = models.OneToOneField(User, primary_key=True)

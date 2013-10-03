from django.contrib.auth.decorators import login_required

from account.models import UserAccount
from weibo.models import WeiboBinding, Feed, Profile 

LOGIN_URL = '/profile/login'

@login_required(LOGIN_URL)
def bind_account(request):
    user_account = UserAccount.objects.get(user=request.user)
    try:
        binding = WeiboBinding.objects.get()
    except WeiboBinding.DoesNotExist:
        binding = WeiboBinding.objects.create()
    except:
        binding = None

@login_required(LOGIN_URL)
def myfeed_feed(request):
    pass

@login_required(LOGIN_URL)
def timeline_feed(request):
    pass

@login_required(LOGIN_URL)
def archive_feed(request):
    pass

from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

from utils.view_decorators import json_view
from weibo.models import WeiboBinding, Profile
from account.models import UserAccount

#==========================================================================================================

def status_view(request):
    if request.user.is_authenticated():
        return dict(loged_in=True)
    else:
        return dict(loged_in=False)


def register_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    uid = request.POST.get('uid', '')
    token = request.POST.get('token', '')
    email = ''

    user = User.objects.create_user(username, email, password)
    account = UserAccount.objects.create(user=user)
    profile, is_new = Profile.objects.get_or_create(uid=uid)
    binding = WeiboBinding.objects.create(bind_account=account, bind_profile=profile, token=token)
    user = auth.authenticate(username=username, password=password)
    auth.login(request, user)
    
    return HttpResponse("Registration and Login success!")


def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')        
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponse('Login Success')
    else:
        return HttpResponse('Login Failed')


def logout_view(request):
    auth.logout(request)
    return HttpResponse('Loged out')
    

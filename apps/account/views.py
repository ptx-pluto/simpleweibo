from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

from utils.view_decorators import rest_api
from weibo.models import WeiboBinding, Profile
from account.models import UserAccount

#==========================================================================================================

@rest_api
def account_view(request):
    if request.method == 'GET': # fetch account info and login status

        if request.user.is_authenticated():
            return { 'login': True, 'status': True }
        else:
            return { 'login': False, 'status': False }

    elif request.method == 'PATCH': # bind weibo account

        uid = request.POST.get('uid', '')
        token = request.POST.get('token', '')

        if request.user.is_authenticated():
            account = request.user.account
            profile, is_new = Profile.objects.get_or_create(uid=uid)
            binding = WeiboBinding.objects.create(bind_account=account, bind_profile=profile, token=token)
            return { 'login': True, 'status': True }
        else:
            return { 'login': False, 'status': False, 'error': 'login' }


def register_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    uid = request.POST.get('uid', '')
    token = request.POST.get('token', '')
    email = ''

    resp = {}

    user = User.objects.get(username=username)
    if user is None:
        user = User.objects.create_user(username, email, password)
        account = UserAccount.objects.create(user=user)
        profile, is_new = Profile.objects.get_or_create(uid=uid)
        binding = WeiboBinding.objects.create(bind_account=account, bind_profile=profile, token=token)
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        return { 'login': True, 'status': True }
    else:
        return { 'login': False, 'status': False, 'error': 'username' }
    

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
    

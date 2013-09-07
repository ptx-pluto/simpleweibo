from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

from apps.profile.models import WeiboBinding
from apps.weibo.models import WeiboProfile

#==========================================================================================================

def status_view(request):
    if request.user.is_authenticated():
        return HttpResponse('You are loged in')
    else:
        return HttpResponse('You are not loged in')


def login_view(request):
    if 'username' not in request.POST or 'password' not in request.POST:
        return render_to_response('login.html', {})
    else:
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
    

def register_view(request):
    if 'username' not in request.POST or 'password' not in request.POST or 'email' not in request.POST:
        return render_to_response('register.html', {})
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email    = request.POST.get('email', '')    
        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse("Registration success!")


@login_required(login_url='/auth/login')
def bind_view(request):
    if 'uid' not in request.POST or 'token' not in request.POST:
        return render_to_response('bind.html', {})
    else:
        uid, token = (request.POST.get('uid',''), request.POST.get('token',''))
        try :
            profile = WeiboProfile.objects.get(uid=uid)
        except WeiboProfile.DoesNotExist:
            profile = WeiboProfile.objects.create( uid=uid, content='' )
        try:
            WeiboBinding.objects.get( user=request.user, profile=profile)
            return HttpResponse('This Weibo account is already binded!')
        except WeiboBinding.DoesNotExist:
            WeiboBinding.objects.create( user=request.user, profile=profile, token=token )
            return HttpResponse('Account binded successfully!')


@login_required(login_url='/auth/login')
def detail_view(request):
    return HttpResponse("content that only loged in user can see")        


@login_required(login_url='/auth/login')
def content_view(request):
    return HttpResponse("content that only loged in user can see")        

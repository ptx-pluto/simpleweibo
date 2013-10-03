from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

from utils.view_decorators import json_view

#==========================================================================================================

@json_view
def status_view(request):
    if request.user.is_authenticated():
        return dict(loged_in=True)
    else:
        return dict(loged_in=False)

@json_view
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

@json_view
def logout_view(request):
    auth.logout(request)
    return HttpResponse('Loged out')
    
@json_view
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


@login_required(login_url='/profile/login')
def detail_view(request):
    return HttpResponse("content that only loged in user can see")        


@login_required(login_url='/profile/login')
def content_view(request):
    return HttpResponse("content that only loged in user can see")        

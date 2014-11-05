from django.shortcuts import render_to_response
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from settings import STATIC_URL
from tags.forms import updateform
from django.template import RequestContext
from tags.models import *

def index(request):
	if request.user.is_authenticated():
		args={}
		args['cur'] = Userprofile.objects.get(user=request.user)
		
		return render_to_response('loggedin.html',args)
	else:
		return render_to_response('index.html')


def logout(request):
	auth_logout(request)
	return index(request)

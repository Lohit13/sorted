from django.shortcuts import render_to_response
from django.contrib.auth import logout as auth_logout
from django.contrib import auth

def index(request):
	if request.user.is_authenticated():
		return render_to_response('loggedin.html')
	else:
		return render_to_response('index.html')


def logout(request):
	auth_logout(request)
	return index(request)

from django.shortcuts import render_to_response
from django.contrib.auth import logout as auth_logout
from django.contrib import auth

def index(request):
	return render_to_response('index.html')

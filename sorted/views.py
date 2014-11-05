from django.shortcuts import render_to_response
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from settings import STATIC_URL
from tags.forms import updateform

def index(request):
	return render_to_response('index.html')

from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from settings import STATIC_URL
from tags.forms import *
from django.template import RequestContext
from tags.models import *

def index(request):
	if request.user.is_authenticated():
		args={}
		try:
			cur = Userprofile.objects.get(user=request.user)
		except:
			return redirect('/update')

		try:
			args['cur'] = Userprofile.objects.get(user=request.user)
			try:
				partner = allocatedBtech1.objects.get(user1 = cur)
				args['partner'] = partner
				args['done'] = 1
				print "found a"
			except:
				try:
					partner = allocatedBtech1.objects.get(user2 = cur)
					args['partner'] = partner
					args['done'] = 1
					print "found a"
				except:
					args['done'] = 0
					print "not found"

			return render_to_response('loggedin.html',args)
		except:
			return redirect('/update')
	else:
		return render_to_response('index.html')


def logout(request):
	auth_logout(request)
	return index(request)

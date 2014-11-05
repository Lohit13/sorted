from django.shortcuts import render_to_response
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from forms import *
from django.core.context_processors import csrf

def update(request):
	if request.user.is_authenticated():
		form = updateform()

		if request.method == "POST":
			print "woohoo"
		args = {}
		args.update(csrf(request))
		args['form'] = form

		return render_to_response('update.html',args)

	else:
		return HttpResponse("doesnt work")
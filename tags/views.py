from django.shortcuts import render_to_response
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from forms import *
from django.shortcuts import render, redirect
from django.core.context_processors import csrf

import unirest


def editpref(request):
	if request.user.is_authenticated():
		args = {}
		args.update(csrf(request))
		if request.method == "POST":

			




		return render_to_response('pref.html',args)
	else:
		return redirect('/')



def update(request):
	if request.user.is_authenticated():

		form = updateform(initial = {'email':request.user.email})
		form.fields['email'].widget.attrs['readonly'] = True

		if request.method == "POST":


			try:
				curruser = Userprofile.objects.get(user = request.user)

				curruser.fname = request.POST['fname']
				curruser.lname = request.POST['lname']
				curruser.batch = request.POST['batch']
				curruser.phno = request.POST['phno']
				curruser.email = request.user.email

				message = "Hello "+request.POST['fname']+","+"your information has been updated"
				message = message.replace(' ','+')
				receiver = request.POST['phno']
				response = unirest.get("https://site2sms.p.mashape.com/index.php?msg="+ message + "&phone="+ receiver +"&pwd=freesms&uid=8860803480",
				 headers={
	    			"X-Mashape-Key": "eaf4vRx8KQmsh3G8S2OgJWmFHKRup103Hhkjsnh2zCKRW67wxp"
	  				}
				)			

			except:
				curruser = Userprofile(user = request.user)
				print "new"
				message = "Hello "+request.POST['fname']+","+" thank you for registering"
				message = message.replace(' ','+')
				receiver = request.POST['phno']
				response = unirest.get("https://site2sms.p.mashape.com/index.php?msg="+ message + "&phone="+ receiver +"&pwd=freesms&uid=8860803480",
				 headers={
	    			"X-Mashape-Key": "eaf4vRx8KQmsh3G8S2OgJWmFHKRup103Hhkjsnh2zCKRW67wxp"
	  				}
				)			

				curruser.fname = request.POST['fname']
				curruser.lname = request.POST['lname']
				curruser.batch = request.POST['batch']
				curruser.phno = request.POST['phno']
				curruser.email = request.user.email

			curruser.save()

			print "woohoo"
		args = {}
		args.update(csrf(request))
		args['form'] = form

		return render_to_response('update.html',args)

	else:
		return HttpResponse("doesnt work")

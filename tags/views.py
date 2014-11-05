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
		curruser = Userprofile.objects.get(email = request.user.email)
		args = {}
		args.update(csrf(request))
		if request.method == "POST":
			try:
				currtag = Tagset.objects.get(user = curruser, tag = Tag.objects.get(tagname = request.POST['course'].lower()))
			except:
				newtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = request.POST['course'].lower()))
				newtag.save()

			if request.POST['waketime'] > 8:
				try:
					currtag = Tagset.objects.get(user = curruser, tag = Tag.objects.get(tagname = "latewake"))
				except:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "latewake"))
					currtag.save()
			else:
				try:
					currtag = Tagset.objects.get(user = curruser, tag = Tag.objects.get(tagname = "earlywake"))
				except:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "earlywake"))
					currtag.save()
			
			if request.POST['sleeptime'] > 2:
				try:
					currtag = Tagset.objects.get(user = curruser, tag = Tag.objects.get(tagname = "latesleep"))
				except:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "latesleep"))
					currtag.save()
			else:
				try:
					currtag = Tagset.objects.get(user = curruser, tag = Tag.objects.get(tagname = "earlysleep"))
				except:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "earlysleep"))
					currtag.save()


			if request.POST['goout']>8:
				try:
					currtag = Tagset.objects.get(user = curruser, tag = Tag.objects.get(tagname = "highgo"))
				except:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "highgo"))
					currtag.save()

			elif request.POST['goout']>4:
				try:
					currtag = Tagset.objects.get(user = curruser, tag = Tag.objects.get(tagname = "midgo"))
				except:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "midgo"))
					currtag.save()
			else:
				try:
					currtag = Tagset.objects.get(user = curruser, tag = Tag.objects.get(tagname = "lowgo"))
				except:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "lowgo"))
					currtag.save()

			for i in Tagset.objects.filter(user = curruser):
				print i.tag.tagname

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
				if(request.POST['phno']):
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
				if(request.POST['phno']):
					curruser.phno = request.POST['phno']
				curruser.email = request.user.email

			curruser.save()
		args = {}
		args.update(csrf(request))
		args['form'] = form

		return render_to_response('update.html',args)

	else:
		return HttpResponse("doesnt work")

from django.shortcuts import render_to_response
from django.contrib.auth import logout as auth_logout
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from forms import *
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
import itertools
from itertools import combinations

import unirest


def editpref(request):
	if request.user.is_authenticated():
		try:
			curruser = Userprofile.objects.get(email = request.user.email)
		except:
			return redirect('/update')
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

		return render_to_response('pref.html',args)
	else:
		return redirect('/')

def count(request):
	master = Tagset.objects.all()

	arr = []

	for i in Userprofile.objects.filter(batch = "2014"):
		if i.id not in arr:
			arr.append(i.id)

	arr = [",".join(map(str,comb)) for comb in combinations(arr, 2)]

	for i in arr:
		a = i[0]
		b = i[2]
		tagset1 = []
		tagset2 = []
		for i in Tagset.objects.filter(user = Userprofile.objects.get(id = a)):
			tagset1.append(i.tag.tagname)
		for i in Tagset.objects.filter(user = Userprofile.objects.get(id = b)):
			tagset2.append(i.tag.tagname)
		countit = len(list(set(tagset1) & set(tagset2)))
		try:
			newbtech1 = Btech1.objects.get(user1 = Userprofile.objects.get(id = a),user2 = Userprofile.objects.get(id = b),count = countit )
		except:
			newbtech1 = Btech1(user1 = Userprofile.objects.get(id = a),user2 = Userprofile.objects.get(id = b),count = countit )
			newbtech1.save()

	return redirect('/')

def allocate(request):

	master = Btech1.objects.all()

	a = []
	b = []
	c = []

	for i in master:
		a.append(i.user1.id)
		b.append(i.user2.id)
		c.append(i.count)


	even = (0 if len(a)%2 else 1) + 1
	half = (len(a)-1)/2
	median = sum(sorted(c)[half:half+even])/float(even)


	for i in range(0,len(c)):
		c[i]-=median
		if c[i]<0:
			c[i]*=(-1)


	class match(object):
		def __init__(self,user1,user2,count):
			self.user1 = user1
			self.user2 = user2
			self.count = count

	table = []
	for i in range(len(a)):
		table.append(match(a[i],b[i],c[i]))					
	table.sort(key = lambda x:x.count)						

	final = []

	while(len(table)):
		final.append(table[0])
		usera = table[0].user1
		userb = table[0].user2
		table = [j for j in table if j.user1 != usera and j.user2 != userb and j.user1 != userb and j.user2 != userb]

	for i in final:
		try:
			allocatedBtech1.objects.get(user1 = Userprofile.objects.get(id = i.user1),user2 = Userprofile.objects.get(id = i.user2))
		except:
			newone = allocatedBtech1(user1 = Userprofile.objects.get(id = i.user1),user2 = Userprofile.objects.get(id = i.user2))
			newone.save()

	return redirect('/')


def adminall(request):
	if request.user.is_authenticated():
		try:
			curruser = Userprofile.objects.get(user = request.user)
			if curruser.role==1:
				args['master'] = allocatedBtech1.objects.all()
				return render_to_response('admin.html',args)
			else:
				return redirect('/')
		except:
			return redirect('/')
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
				curruser.address = request.POST['address']
				if(request.POST['phno']):
					curruser.phno = request.POST['phno']
				curruser.email = request.user.email

				message = "Hello "+request.POST['fname']+","+"your information has been updated"
				print response	

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
				curruser.address = request.POST['address']
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

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

			if( Tagset.objects.filter( user = curruser, tag = Tag.objects.get(tagname = request.POST['course'].lower())).exists() ):
				print "FIIFIFIFIF"
			else:	
				newtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = request.POST['course'].lower()))
				newtag.save()
				print "YAYAYA"

			if request.POST['waketime'] > 8:
				if ( Tagset.objects.filter(user = curruser, tag = Tag.objects.get(tagname = "latewake")).exists()):
					pass
				else:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "latewake"))
					currtag.save()
			else:
				if ( Tagset.objects.filter(user = curruser, tag = Tag.objects.get(tagname = "earlywake")).exists()):
					pass
				else:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "earlywake"))
					currtag.save()			
			if request.POST['sleeptime'] > 2:
				if ( Tagset.objects.filter(user = curruser, tag = Tag.objects.get(tagname = "latesleep")).exists()):
					pass
				else:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "latesleep"))
					currtag.save()
			else:
				if ( Tagset.objects.filter(user = curruser, tag = Tag.objects.get(tagname = "earlysleep")).exists()):
					pass
				else:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "earlysleep"))
					currtag.save()			


			if request.POST['goout']>8:
				if (Tagset.objects.filter(user = curruser, tag = Tag.objects.get(tagname = "highgo")).exists()):
					pass
				else:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "highgo"))
					currtag.save()

			elif request.POST['goout']>4:
				if (Tagset.objects.filter(user = curruser, tag = Tag.objects.get(tagname = "midgo")).exists()):
					pass
				else:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "midgo"))
					currtag.save()
			else:
				if (Tagset.objects.filter(user = curruser, tag = Tag.objects.get(tagname = "lowgo")).exists()):
					pass
				else:
					currtag = Tagset(user = curruser, tag = Tag.objects.get(tagname = "lowgo"))
					currtag.save()

		return render_to_response('pref.html',args)
	else:
		return redirect('/')

def count(request):
	if request.user.is_authenticated():	
		curruser = Userprofile.objects.get(user=request.user)
		if curruser.role==1:
			print "admin beta"
			master = Tagset.objects.all()

			arr = []

			for i in Userprofile.objects.filter(batch = "2014"):
				if i.id not in arr:
					arr.append(i.id)

			arr = [",".join(map(str,comb)) for comb in combinations(arr, 2)]
			print arr
			for i in arr:
				c = i.split(',')
				print c
				a = c[0]
				b = c[1]
				tagset1 = []
				tagset2 = []
				if a!= curruser.id and b!= curruser.id:
					try:
						for i in Tagset.objects.filter(user = Userprofile.objects.get(id = a)):
							tagset1.append(i.tag.tagname)
					except:
						pass
					try:
						for i in Tagset.objects.filter(user = Userprofile.objects.get(id = b)):
							tagset2.append(i.tag.tagname)
					except:
						pass
					countit = len(list(set(tagset1) & set(tagset2)))
					print tagset1,tagset2
					print countit
					print a,b
					u = Userprofile.objects.get(id = a)
					v = Userprofile.objects.get(id = b)
					print u,v
					newbtech1 = Btech1(user1 = u,user2 = v ,count = countit)

					try:
						newbtech1 = Btech1.objects.get(user1 = Userprofile.objects.get(id = a),user2 = Userprofile.objects.get(id = b),count = countit )
					except:
						newbtech1 = Btech1(user1 = Userprofile.objects.get(id = a),user2 = Userprofile.objects.get(id = b),count = countit )
						newbtech1.save()
		else:
			print "not admin beta"
		return redirect('/')

	else:
		return redirect('/')

def allocate(request):
	curruser = Userprofile.objects.get(user = request.user)
	if curruser.role==1:
		print "admin beta"
		print "LALALALALLA"

		master = Btech1.objects.all()

		a = []
		b = []
		c = []

		for i in master:
			a.append(i.user1.id)
			b.append(i.user2.id)
			c.append(i.count)

		print 
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
		print "\nall possible combinations : \n"
		for i in table:
			print i.user1,i.user2,i.count

		print "\n\n"


 
		while(len(table)):
			final.append(table[0])
			print table
			usera = table[0].user1
			userb = table[0].user2
			table = [j for j in table if j.user1 != usera and j.user2 != userb and j.user1 != userb and j.user2 != userb]

		print "final is\n"
		for i in final:
			print i.user1,i.user2,i.count


		for i in final:
			try:
				allocatedBtech1.objects.get(user1 = Userprofile.objects.get(id = i.user1),user2 = Userprofile.objects.get(id = i.user2))
			except:
				newone = allocatedBtech1(user1 = Userprofile.objects.get(id = i.user1),user2 = Userprofile.objects.get(id = i.user2))
				newone.save()

		print "BABABABABA"
	else:
		print "not admin beta"
	return redirect('/')


def adminall(request):
	if request.user.is_authenticated():
		curruser = Userprofile.objects.get(user = request.user)
		print "one"
		try:
			print "two"
			if curruser.role==True:
				print "three"
				master = []
				for i in allocatedBtech1.objects.all():
					master.append(i)
			return render_to_response('admin.html',{'master':master})	
		except:
			return redirect('/')
	else:
		return redirect('/')

def update(request):
	if request.user.is_authenticated():

		form = updateform(initial = {'email':request.user.email})
		form.fields['email'].widget.attrs['readonly'] = True
		
		try:
			curruser = Userprofile.objects.get(user = request.user)
			if curruser.role == 1:
				return redirect('/adminsite')	
		except:
			pass
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

			except:
				curruser = Userprofile(user = request.user)
				message = "Hello "+request.POST['fname']+","+" thank you for registering"
			
				curruser.fname = request.POST['fname']
				curruser.lname = request.POST['lname']
				curruser.batch = request.POST['batch']
				curruser.address = request.POST['address']
				if(request.POST['phno']):
					curruser.phno = request.POST['phno']
				curruser.email = request.user.email
			message = message.replace(' ','+')
			receiver = request.POST['phno']
			response = unirest.get("https://site2sms.p.mashape.com/index.php?msg="+ message + "&phone="+ receiver +"&pwd=freesms&uid=8130962007",
			 headers={
	    		"X-Mashape-Key": "eaf4vRx8KQmsh3G8S2OgJWmFHKRup103Hhkjsnh2zCKRW67wxp"
	  			}
			)	

			curruser.save()
		args = {}
		args.update(csrf(request))
		args['form'] = form

		return render_to_response('update.html',args)

	else:
		return HttpResponse("doesnt work")

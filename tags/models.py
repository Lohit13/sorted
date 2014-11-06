from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    user = models.ForeignKey(User, unique=True)
    fname = models.CharField(max_length=50, blank=True)
    lname = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)
    batch = models.CharField(max_length=50, blank=True)
    phno = models.BigIntegerField(max_length=10, blank=True, null=True)
    role = models.BooleanField(default=0)
    address = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=20,decimal_places=2,blank=True,null=True,default=0)

class Tag(models.Model):
    tagname = models.CharField(max_length=100)

class Tagset(models.Model):
	user = models.ForeignKey(Userprofile)
	tag = models.ForeignKey(Tag)

class Btech1(models.Model):
	user1 = models.ForeignKey(Userprofile, related_name='1a')
	user2 = models.ForeignKey(Userprofile, related_name='1b')
	count = models.IntegerField(max_length = 5,default = 0)


class Btech2(models.Model):
	user1 = models.ForeignKey(Userprofile, related_name='2a')
	user2 = models.ForeignKey(Userprofile, related_name='2b')
	count = models.IntegerField(max_length = 5,default = 0)

class Btech3(models.Model):
	user1 = models.ForeignKey(Userprofile, related_name='3a')
	user2 = models.ForeignKey(Userprofile, related_name='3b')
	count = models.IntegerField(max_length = 5,default = 0)

class Btech4(models.Model):
	user1 = models.ForeignKey(Userprofile, related_name='4a')
	user2 = models.ForeignKey(Userprofile, related_name='4b')
	count = models.IntegerField(max_length = 5,default = 0)

 




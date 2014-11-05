from django import forms
from django.forms.widgets import *
from models import *

BATCH = (
	('2014','Btech 1st Year'),
	('2013','Btech 2nd Year'),
	('2012','Btech 3rd Year'),
	('2012','Btech 4th Year'),
	)

COURSE = (
	('ECE','ECE'),
	('CSE','CSE'),
	)

FOOD = (
	('Veg',0),
	('Non-Veg',1),
	)

class updateform(forms.ModelForm):
	email = forms.CharField(required = True, widget = forms.TextInput,label = "email ")
	fname = forms.CharField(required = True, widget = forms.TextInput,label = "Name ")
	lname = forms.CharField(required = True, widget = forms.TextInput,label = "Surname ")
	batch = forms.ChoiceField(required = True, choices = BATCH,label = "Batch ")
	phno = forms.IntegerField(required = True, widget = forms.TextInput,label = "Mobile number ")

	class Meta:
		model = Userprofile
		fields = ('email','fname','lname','batch','phno')

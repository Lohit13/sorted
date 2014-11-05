from django import forms
from django.forms.widgets import *
from models import *

BATCH = (
	('2014','Btech 1st Year'),
	('2013','Btech 2nd Year'),
	('2012','Btech 3rd Year'),
	('2012','Btech 4th Year'),
	)


class updateform(forms.ModelForm):
	email = forms.CharField(required = True, widget = forms.TextInput)
	fname = forms.CharField(required = True, widget = forms.TextInput)
	lname = forms.CharField(required = True, widget = forms.TextInput)
	batch = forms.ChoiceField(required = True, choices = BATCH)
	phno = forms.IntegerField(required = True, widget = forms.TextInput)

	class Meta:
		model = Userprofile
		fields = ('email','fname','lname','batch','phno')

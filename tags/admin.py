from django.contrib import admin
from tags.models import *

# Register your models here.

Models = [Userprofile,Tag,Tagset,Btech1,Btech2,Btech3,Btech4]

admin.site.register(Models)








from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sorted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),

    url(r'^$', 'sorted.views.index', name='home'), #index page

    url(r'^logout/', 'sorted.views.logout'),


    url(r'^update/', 'tags.views.update', name = 'update'),
    url(r'^editpreferences/', 'tags.views.editpref', name = 'editpref'),
    url(r'^count/', 'tags.views.count', name = 'count'),
    url(r'^allocate/', 'tags.views.allocate', name = 'allocate'),


)

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	# set app at root
    url(r'', include('commentBoard.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

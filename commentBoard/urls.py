from django.conf.urls import patterns, url
from commentBoard import views

urlpatterns =  patterns('',
	url(r'^$', views.index, name = 'perk.index'),
	url(r'^(?P<post_id>\d+)/$', views.post, name = 'perk.post'),
	url(r'^(?P<post_id>\d+)/postVote/$', views.postVote, name = 'perk.post.vote'),
	url(r'^(?P<post_id>\d+)/commentVote/$', views.commentVote, name= 'perk.comment.vote'),
)
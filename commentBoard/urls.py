from django.conf.urls import patterns, url
from commentBoard import views

urlpatterns =  patterns('',
	# our main view
	url(r'^$', views.index, name = 'perk.index'),
	# look at one post
	url(r'^(?P<post_id>\d+)/$', views.post, name = 'perk.post'),
	# vote on post
	url(r'^(?P<post_id>\d+)/postVote/$', views.postVote, name = 'perk.post.vote'),
	# vote on comment
	url(r'^(?P<post_id>\d+)/commentVote/$', views.commentVote, name= 'perk.comment.vote'),
)
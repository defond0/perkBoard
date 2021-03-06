import logging
logging.basicConfig()
logger = logging.getLogger("KennyLoggin")
from django.shortcuts import *
from django.http import HttpResponse
from commentBoard.models import Post
from commentBoard.models import Comment
from commentBoard.models import User
from commentBoard.forms import postForm,commentForm


def index(request):
	context = {}
	# Handle POSTS
	if request.method == 'POST':
		form = postForm(request.POST)
		if form.is_valid():
			#create post and show its view page
			context['post']=savePost(form.cleaned_data)
			context['comments']=getComments(context['post'].id)
			context['form']=commentForm()
			return render(request, 'commentBoard/post.html',context)
		else:
			#report error
			postList = Post.objects.order_by('-score')
			context['postList']=postList
			context['form']=postForm()
			context['errors']=["POST FAILURE: One Or More Fields Missing",]
			return render(request, 'commentBoard/index.html',context)
	# Handle GETS
	else:
		postList = Post.objects.order_by('-score')
		context['postList']=postList
		context['form']=postForm()
		return render(request,'commentBoard/index.html',context)


def post(request, post_id):
	p = Post.objects.get(id=post_id)
	c = getComments(p.id)
	context={'comments':c, 'post':p, 'form':commentForm()}
	# Handle POSTS
	if request.method == 'POST':
		form = commentForm(request.POST)
		if form.is_valid():
			#create comment 
			comment=saveComment(form.cleaned_data,p)
			return redirect('/'+str(p.id))
		else:
			#report error
			context['errors']=["COMMENT FAILURE: One Or More Fields Missing",]
			return render(request, 'commentBoard/post.html',context)
	# Handle GETS
	else:
		return render(request, 'commentBoard/post.html',context)


def postVote(request, post_id):
	p = Post.objects.get(id=post_id)
	# if upvote increment score otherwise decrement
	if request.POST.get("up")=="true":
		p.score +=1
	else:
		p.score -=1
	p.save();
	return redirect('/')

def commentVote(request,post_id):
	commentId=request.POST.get("id")
	c = Comment.objects.get(id=commentId)
	# if upvote increment score otherwise decrement
	if request.POST.get("up")=="true":
		c.score +=1
	else:
		c.score -=1
	c.save();
	return redirect('/'+str(post_id))

def savePost(data):
	# helper function to save post
	try:
		u = User.objects.get(name=data['user'])
	except User.DoesNotExist:
		u = User.objects.create(name=data['user'])
	finally:
		p = Post.objects.create(content=data['content'],user =u)
		return p


def getComments(id):
	# helper function to get comments associated with post
	try:
		comments = Comment.objects.filter(post=id).order_by('-score')
	except Comment.DoesNotExist:
		comments = []
	finally:
		return comments

def saveComment(data, post):
	#helper function to save comment
	try:
		u = User.objects.get(name=data['user'])
	except User.DoesNotExist:
		u = User.objects.create(name=data['user'])
	finally:
		c = Comment.objects.create(content=data['content'],user =u, post=post)
		return c




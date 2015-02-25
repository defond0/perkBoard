from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class Post(models.Model):
	content = models.CharField(max_length=400, default="")
	score = models.IntegerField(default=0)
	user = models.ForeignKey(User)

	def __str__(self):
		return self.content

class Comment(models.Model):
	content = models.CharField(max_length=400, default="")
	score = models.IntegerField(default=0)
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)

	def __str__(self):
		return self.content
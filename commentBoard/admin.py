from django.contrib import admin
from commentBoard.models import User
from commentBoard.models import Post
from commentBoard.models import Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
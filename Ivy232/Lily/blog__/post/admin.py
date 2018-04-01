from django.contrib import admin
from .models import Post, Comment, ProgrammingCategory

admin.site.register(Post)
#This is the post section in admin

admin.site.register(Comment)
#This is the Comment section we recently added.

admin.site.register(ProgrammingCategory)
# Register your models here.

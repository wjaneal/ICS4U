
from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
#This is to define a form for each of the posts.

    class Meta:
        model = Post#This is to stipulate which model the form corresponds to.
        fields = ('title', 'text',)#This is to set variables of title and text.

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment#This is to stipulate which model the form corresponds to.
        fields = ('author', 'text',)#This is to set variables of title and text.



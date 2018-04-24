
from django import forms
#This is to import module for organizing form.
from .models import Post, Comment
#This is to show the models that we want to create form for.
#The models have already been created in the file "model.py"
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)



from django.shortcuts import render
from django.utils import timezone

from .models import Post
#
from django.http import HttpResponseRedirect, HttpResponse

from django.template import loader

from django.shortcuts import get_object_or_404, render

from django.urls import reverse

# The dot before models means current directory or current application
# This means we can use . and the name of the file (without .py).
# Then we import the name of the model (Post).

# Main Page
def main_page(request):
    return render(request, 'blog/main_page.html')
# Content
'''
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
'''
def post_list(request):
    posts = Post.objects.filter(category__contains='English').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
# We create a variable for our QuerySet: posts.
# Treat this as the name of our QuerySet. From now on we can refer to it by this name.
    
def post_list2(request):
    posts2 = Post.objects.filter(category__contains='Physics').order_by('published_date')
    return render(request, 'blog/post_list2.html', {'posts2': posts2})

def post_list3(request):
    posts3 = Post.objects.filter(category__contains='Chemistry').order_by('published_date')
    return render(request, 'blog/post_list3.html', {'posts3': posts3})
'''
def detail_page(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)
def detail_page(request):
    return render(request,'blog/detail_page.html')
'''

def detail_page(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail_page.html', {'post': post})


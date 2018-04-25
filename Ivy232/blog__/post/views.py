from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post/post_list.html',{'posts': posts})
#This is to show the list (title) of all the posts.
    Post.objects.get(pk=pk)
#This is to organize and show all of the posts in the time sequence.
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
#This is to get detail page or show the 404-not-found page.
    return render(request, 'post/post_detail.html', {'post':post})
#This is to create a route directing to corresponding detail pages.

def post_new(request):
    form = PostForm()
    return render(request, 'post/post_edit.html', {'form': form})
#This is to create a link to the edit page which should be using a certain form we created.
    if request.method == "POST":
        form = PostForm(request.POST)
    else:
        form = PostForm()
#This is to use the method of POST.
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)
#Return to the newly created pages.
    else:
        form = PostForm()
    return render(request, 'post/post_edit.html', {'form': form})
#The edit page will stay if the info put in does not meet the requirement of the form.
def post_edit(request, pk): #to create the function of editing the post
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)#save the form
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user#This is to save the name of author.
            post.published_date = timezone.now()#This is to save the current time.
            post.save()#This to save the post.
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)#open the form
    return render(request, 'post/post_edit.html', {'form': form})
#The edit page will stay if the info put in does not meet the requirement of the form.
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)#This is to create a route directing to corresponding detail pages.
    else:
        form = CommentForm()
    return render(request, 'post/add_comment_to_post.html', {'form': form})
#The edit page will stay if the info put in does not meet the requirement of the form.
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def post_remove_succeed(request, pk):
    return render(request, 'post/diy.html', {})
'''
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
'''
# Create your views here.

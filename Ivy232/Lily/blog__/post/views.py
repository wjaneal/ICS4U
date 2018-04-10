from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #Filter() gives us a QuerySet, so does objects.get()
    #Post of all the time point less than NOW (posted in the past) will be showen in the page.
    return render(request, 'post/post_list.html',{'posts': posts})
    #This is to use the template and designate a variable name for the info we filtered out.
    Post.objects.get(pk=pk)
    #
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    #Connect the post_detail to the post.
    return render(request, 'post/post_detail.html', {'post':post})
    #This is to use the template and designate a variable name for the info we filtered out. Show the detailed page of the post.
def post_new(request):
    form = PostForm()
    #Pass the form we created in the file "form.py" to this function
    #The information that the user will type in will follow the form.
    return render(request, 'post/post_edit.html', {'form': form})
    #Provide a template for this page. Pass the form to the variable "form".
    if request.method == "POST":#This is a certain method in django.
    #If the method is POST, we want to construct the Postform() with data from the form.
        form = PostForm(request.POST)
    else:
        form = PostForm()
    
    if form.is_valid():#The info should be complete:author, time, content, etc.
        post = form.save(commit=False)
        #We don't want to save the Post model first. We want to add author first
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)
        #This is to go to the post newly created, which follow the template "post_detail".

    else:
        form = PostForm()
    return render(request, 'post/post_edit.html', {'form': form})
    #If the info is not complete, the user is required to complete the info, or the post will not be created successfully.

def post_edit(request, pk): #to create the function of editing the post
    post = get_object_or_404(Post, pk=pk) #This is to go to certain post so that the user can do modification. Page of 404_not_found is included.
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)#save the form
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)#open the form
    return render(request, 'post/post_edit.html', {'form': form})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
    #GET and POST are the only HTTP methods to use when dealing with forms.
    #Any request that could be used to change the state of the system - for example, a request that makes changes in the database - should use POST. GET should be used only for requests that do not affect the state of the system.
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)#This is to save the content.
            comment.post = post#This is to state the comment belongs to certain post.
            comment.save()#This is to save the comment.
            return redirect('post_detail', pk=post.pk)#This is to show the page after adding comment to it.
    else:
        form = CommentForm()#This is to require the user to enter all the necessary info defined in the form.
    return render(request, 'post/add_comment_to_post.html', {'form': form})#This is to keep the user stay at the page to add comment until all the info is available.

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)#This is to pinpoint a certain post.
    post.delete()#This is to delete the post.
    return redirect('post_list') #This is to return back to the homepage.

def post_remove_succeed(request, pk):
    return render(request, 'post/diy.html', {})
    #This is an aborted trial =(
    #This is to try to direct the user to a page saying "You have deleted the post successfully!!".
def face(request):
    post = get_object_or_404(Post)
    return render(request, 'post/face.html', {'post':post})
    #This is an aborted trial =(
    #This is to try to direct the user to a real homepage with three catagories-English4U, Physics, and Chemistry.
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

from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Main Page
def main_page(request):
    return render(request, 'post/main_page.html')
'''
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post/post_list.html',{'posts': posts})
    Post.objects.get(pk=pk)
'''
def post_list(request):
    posts = Post.objects.filter(category__contains='English').order_by('published_date')
    return render(request, 'post/post_list.html', {'posts': posts})
def post_list2(request):
    posts2 = Post.objects.filter(category__contains='Physics').order_by('published_date')
    return render(request, 'post/post_list2.html', {'posts2': posts2})
def post_list3(request):
    posts3 = Post.objects.filter(category__contains='Chemistry').order_by('published_date')
    return render(request, 'post/post_list3.html', {'posts3': posts3})


def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post':post})

def post_new(request):
    form = PostForm()
    return render(request, 'post/post_edit.html', {'form': form})
    if request.method == "POST":
        form = PostForm(request.POST)
    else:
        form = PostForm()

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()
    return render(request, 'post/post_edit.html', {'form': form})

def post_edit(request, pk): #to create the function of editing the post
    post = get_object_or_404(Post, pk=pk)
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

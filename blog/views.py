from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Page
from .forms import PageForm
from .forms import PostForm

def post_list(request):
    page = Page.objects.filter(visited=False, memory=False)
    print(page)
    posts = Post.objects.filter(published_date__lte=timezone.now(), visited=False, memory=False).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'page': page})

def dest_list(request):
    page = Page.objects.filter(visited=True, memory=False)
    posts = Post.objects.filter(published_date__lte=timezone.now(), visited=True).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'page': page})

def memory_list(request):
    page = Page.objects.filter(visited=False, memory=True)
    posts = Post.objects.filter(published_date__lte=timezone.now(), memory=True).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'page': page})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def page(request):
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return render('blog/post_list.html', {})
    else:
        form = PageForm()
    return render(request, 'blog/page_edit.html', {'form': form})    
            

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form': form})    
from django.shortcuts import render, get_object_or_404,redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'main/home.html',{})

def ec(request):
    return render(request, 'main/ec.html',{})

def ecaiis(request):
    return render(request, 'main/ecaiis.html',{})

def eccvr(request):
    return render(request, 'main/eccvr.html',{})
    
def molding(request):
    return render(request, 'main/molding.html',{})


# pyscript テスト用
def pyscript_test(request):
    return render(request, 'pyscript_test/pyscript_test.html', {})

def display(request):
    return render(request, 'pyscript_test/display.html', {})

def py_repl(request):
    return render(request, 'pyscript_test/py_repl.html', {})

def element(request):
    return render(request, 'pyscript_test/element.html', {})
    
def get_event(request):
    return render(request, 'pyscript_test/get_event.html', {})
    
def split_module(request):
    return render(request, 'pyscript_test/split_module.html', {})
    
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid(): # フォームの値が有効である場合、
            post = form.save(commit=False) # フォームに入力された値を一時格納（commit=Falseはモデルとして保存していないという意
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
    
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

# テスト
def iot(request):
    return render(request, 'blog/iot.html',{})

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

# javascriptテスト用
def javascript_test(request):
    return render(request, 'javascript_test/home.html',{})

def tutorial(request):
    return render(request, 'javascript_test/tutorial.html',{})

def number_guess(request):
    return render(request, 'javascript_test/number_guess.html',{})

def variable(request):
    return render(request, 'javascript_test/variable.html',{})

def number(request):
    return render(request, 'javascript_test/number.html',{})

def string(request):
    return render(request, 'javascript_test/string.html',{})
    
def array(request):
    return render(request, 'javascript_test/array.html',{})

def Generate_random_story(request):
    return render(request, 'javascript_test/Generate_random_story.html',{})
    
def if_function(request):
    return render(request, 'javascript_test/if_function.html',{})

def loop_function(request):
    return render(request, 'javascript_test/loop_function.html',{})

def loop_function_skillcheck1(request):
    return render(request, 'javascript_test/loop_function_skillcheck1.html',{})

def loop_function_skillcheck2(request):
    return render(request, 'javascript_test/loop_function_skillcheck2.html',{})

def loop_function_skillcheck3(request):
    return render(request, 'javascript_test/loop_function_skillcheck3.html',{})

def usefunction_draw(request):
    return render(request, 'javascript_test/usefunction_draw.html',{})
    
def usefunction_scope(request):
    return render(request, 'javascript_test/usefunction_scope.html',{})
    
def usefunction_skillcheck1(request):
    return render(request, 'javascript_test/usefunction_skillcheck1.html',{})

def usefunction_skillcheck2(request):
    return render(request, 'javascript_test/usefunction_skillcheck2.html',{})

def usefunction_skillcheck3(request):
    return render(request, 'javascript_test/usefunction_skillcheck3.html',{})

def usefunction_skillcheck4(request):
    return render(request, 'javascript_test/usefunction_skillcheck4.html',{})

def ownfunction(request):
    return render(request, 'javascript_test/ownfunction.html',{})

def return_function1(request):
    return render(request, 'javascript_test/return_function1.html',{})
    
def return_function2(request):
    return render(request, 'javascript_test/return_function2.html',{})

def event_listener(request):
    return render(request, 'javascript_test/event_listener.html',{})

def event_video(request):
    return render(request, 'javascript_test/event_video.html',{})

def event_tile(request):
    return render(request, 'javascript_test/event_tile.html',{})

def event_skillcheck1(request):
    return render(request, 'javascript_test/event_skillcheck1.html',{})

def event_skillcheck2(request):
    return render(request, 'javascript_test/event_skillcheck2.html',{})

def event_skillcheck3(request):
    return render(request, 'javascript_test/event_skillcheck3.html',{})
    
def gallery(request):
    return render(request, 'javascript_test/gallery.html',{})

def object_basic(request):
    return render(request, 'javascript_test/object_basic.html',{})

def object_skillcheck1(request):
    return render(request, 'javascript_test/object_skillcheck1.html',{})

def object_skillcheck2(request):
    return render(request, 'javascript_test/object_skillcheck2.html',{})

def object_skillcheck3(request):
    return render(request, 'javascript_test/object_skillcheck3.html',{})
    
def object_prototype(request):
    return render(request, 'javascript_test/object_prototype.html',{})
    
def object_oriented_programming(request):
    return render(request, 'javascript_test/object_oriented_programming.html',{})

def object_oriented_programming_skillcheck(request):
    return render(request, 'javascript_test/object_oriented_programming_skillcheck.html',{})

def working_with_json(request):
    return render(request, 'javascript_test/working_with_json.html',{})

def working_with_json_skillcheck(request):
    return render(request, 'javascript_test/working_with_json_skillcheck.html',{})

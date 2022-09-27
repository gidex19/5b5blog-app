from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm, MyTestForm, CreatePostForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    posts = Post.objects.all()   
    return render(request, 'my_app/home.html', {'all_posts': posts})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f"Hello {username}, Your account has been created successfully")
            return redirect('homepage')
    else:
        form = SignUpForm()    
    return render(request, 'my_app/signup.html', {'form': form} )

def blocktest(request):
    request.user
    all_posts = Post.objects.all()
    last_post = Post.objects.last()
    context = {
        'all_posts': all_posts,
        'lastpost': last_post
    }
    return render(request, 'my_app/blocktest.html', context)  
    
def post_detail(request, pk):
    the_post = Post.objects.filter(id=pk).first()
    return render(request, 'my_app/post-detail.html', {'post': the_post})

@login_required
def createpost(request):
    user = request.user
    if request.method == 'POST':
        form  = CreatePostForm(request.POST)
        if form.is_valid():
            form_title = form.cleaned_data.get('title')
            form_body = form.cleaned_data.get('body')
            # form.save(owner = user)
            Post.objects.create(title=form_title, body = form_body, owner = user)
            messages.success(request, "Post created successfully")
            return redirect('homepage')
    else:
        form = CreatePostForm()
    return render(request, 'my_app/testform.html', {'form': form})    

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post


class ClassCreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']
        
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClassUpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']
        
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.owner == self.request.user:
            return True
        else:
            return False


class ClassDeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if post.owner == self.request.user:
            return True
        else:
            return False



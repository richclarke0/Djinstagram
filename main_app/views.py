
from django.shortcuts import render
from .models import Post, Profile
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# from urllib import request
from django.contrib.auth.models import User






# posts = ""

# def home(request):
#     return render(request, 'index.html', { 'posts' : posts })

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', { 'posts': posts })

# class PostList(ListView):
#     model = Post
 


class PostCreate(CreateView):
    model = Post
    fields = '__all__'

    def form_valid(self, form):
    
        success_url = '/posts/'


class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'


class PostDelete(DeleteView):
    model = Post
    success_url = '/post/'

class PostDetail(DetailView):
    model = Post

       



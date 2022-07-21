from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Post

posts = ""

def home(request):
    return render(request, 'index.html', { 'posts' : posts })

def post_index(request):
    cats = Post.objects.all()
    return render(request, 'post/index.html', { 'posts': posts })

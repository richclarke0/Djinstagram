from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# posts = ""

def home(request):
    return render(request, 'index.html')

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', { 'posts': posts })


class PostCreate(CreateView):
  model = Post
  fields = '__all__'

  def form_valid(self, form):
   
    success_url = '/posts/'


class PostUpdate(UpdateView):
    model = Post
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = '__all__'


class PostDelete(DeleteView):
    model = Post
    success_url = '/posts/'

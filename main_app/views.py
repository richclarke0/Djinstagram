
from django.shortcuts import render, redirect
from .models import Post, Profile
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# import uuid
# import boto3

# from urllib import request
from django.contrib.auth.models import User






# posts = ""

def home(request):
    return render(request, 'home.html')

    # return render(request, 'index.html', { 'posts' : posts })
@login_required
def post_index(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'posts/index.html', { 'posts': posts })

# class PostList(ListView):
#     model = Post
@login_required
def post_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'posts/detail.html', { 'post': post })


class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['photo_url', 'caption']
    success_url = '/posts/'

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)




class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Post
    fields = '__all__'
    success_url: 'post_detail'

class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/posts/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = SignUpForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = SignUpForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


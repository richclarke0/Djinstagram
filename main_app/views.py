
from django.shortcuts import render, redirect
from .models import Post, Profile
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin






from django.contrib.auth.models import User

# import uuid
# import boto3

# from urllib import request






# posts = ""

def home(request):
    posts= Post.objects.all()
    return render(request, 'home.html', { 'posts': posts })

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




class PostUpdate(UserPassesTestMixin, LoginRequiredMixin,UpdateView):
    model = Post
    fields = '__all__'
    success_url: 'post_detail'
    def test_func(self):
        self.object = self.get_object() 
        return self.object.user == self.request.user
    def handle_no_permission(self):
        return redirect('home')
    

class PostDelete(UserPassesTestMixin,LoginRequiredMixin, DeleteView,):
    model = Post
    success_url = 'index'
    raise_exception = True

    def test_func(self):
        self.object = self.get_object() 
        return self.object.user == self.request.user
    def handle_no_permission(self):
        return redirect('home')
    


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


class ProfileDetail(LoginRequiredMixin,DetailView):
    model= Profile
    user= User
    def get_absolute_url(self):
    # print(self)
        
        return reverse('profile_detail', kwargs={'pk': self.id})



class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    # user_form = SignUpForm
    profile_form = ProfileForm
    # fields = ['username','profile_picture', 'bio']
    template_name = 'registration/profile-update.html'

    
    def post(self, request, *args, **kwargs):

        post_data = request.POST or None

        # user_form = SignUpForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, instance=request.user.profile)
        if profile_form.is_valid():
            # user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('profile_detail', kwargs={'pk': request.user.id}))

        context = self.get_context_data(
                                        # user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
 


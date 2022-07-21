from django.shortcuts import render
from django.views.generic import ListView, View

posts = ""

def home(request):
    return render(request, 'index.html', { 'posts' : posts })
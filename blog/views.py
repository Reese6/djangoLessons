from django.shortcuts import render
from django.views import generic

from .models import Post


class BlogListView(generic.ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

from pdb import post_mortem
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from base.models import Post


class HomeView(ListView):
    model = Post
    template_name = 'base/index.html' 

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'base/article_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'base/add_post.html'
    fields = '__all__'
    #fields = ('title', 'body')

class StandardView(DetailView):
    model = Post
    template_name = 'base/single_standard.html'

def AboutView(request):
    return render(request, 'base/about.html')

def ContactView(request):
    return render(request, 'base/contact.html')


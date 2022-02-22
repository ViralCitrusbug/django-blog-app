from django import forms
from django.contrib.auth.models import User
from django.http import Http404
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from .models import Post,Category,Image, Profile
from . import formviews

class PostList(ListView):
    model = Post
    context_object_name = "page"
    template_name = 'index.html'
    ordering = ['-published_date']
    paginate_by = 3
    paginate_orphans = 1

    def get_context_data(self,*args, **kwargs):
        try:
            return super(PostList,self).get_context_data(*args,**kwargs)
        except Http404:
            self.kwargs['page']=1
            return super(PostList,self).get_context_data(*args,**kwargs)

class PostDetail(DetailView):
    model = Post
    context_object_name = "post"
    template_name = 'blog_detail.html'

class ProfileView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'profile.html'

class CreateUser(CreateView):
    model = User
    form_class = formviews.SignupForm
    template_name = 'authentication/signup.html'
    success_url = '/login'
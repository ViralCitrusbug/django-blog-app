from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,View,UpdateView,DeleteView
from .models import Post,Category, Profile
from .formviews import *
from .views import category_list
from . models import Comment

class PostList(View):
    def get(self,request):
        post = Post.objects.all().order_by('-published_date')
        category_id = request.GET.get('category')
        search = request.GET.get('search')
        if request.method == "GET":
            if search:
                post = Post.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))
        if category_id:
            post = Post.objects.filter(category=category_id) 
        post_per_page = 3
        paginator = Paginator(post,post_per_page,orphans=1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "posts":post,
            "category":category_list,
            "page":page_obj,
            "paginator":paginator
        }
        return render(request , "index.html", context)

class PostDetail(View):
    def get(self,request,post_id):
        post_detail = Post.objects.get(id=post_id)
        comment = Comment.objects.filter(post=post_detail).order_by('-upload_on')
        context = {
            "post" : post_detail,
            "comments":comment,
            "category":category_list
        }
        return render(request,'blog_detail.html',context)

class ProfileView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'profile.html'

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['picture']
    template_name = 'class/profile.html'
    success_url = "/"

class CreateUser(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'authentication/signup.html'
    success_url = '/user/login'

class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'class/add-blog.html'
    success_url = "/"

class DeletePost(DeleteView):
    model = Post
    success_url = '/blog/create'
from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password,make_password
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,View,UpdateView,DeleteView
from .models import Post,Category, Profile,Image
from .formviews import *
from .views import category_list
from . models import Comment
import re
class PostList(View):
    def get(self,request):
        post = Post.objects.filter(soft_delete=False).order_by('-published_date')
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
        return render(request,'blog-detail.html',context)

class ProfileView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'profile.html'

class ProfileView(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            user_detail = User.objects.get(id=pk)
            post = Post.objects.filter(user = request.user)
            if request.method == "POST":
                Profile.objects.filter(user=request.user).delete()
                image = request.FILES.get('image')
                prof = Profile.objects.create(user=request.user,picture=image)
                prof.save()
            context = {
                "user":user_detail,
                "posts" : post,
                "category":category_list
            }
            return render(request,"profile.html",context)
        else:
            return redirect('login')
class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['picture']
    template_name = 'class/profile.html'
    success_url = "/"

# class CreateUser(CreateView):
#     model = User
#     form_class = SignupForm
#     template_name = 'authentication/signup.html'
#     success_url = '/user/login'

class CreateUser(View):
    def get(self,request):
        context = {
            "category":category_list
        }
        return render(request,'authentication/signup.html',context)
    
    # ##  EMAIL VALIDATION
    # def email_is_valid(email):
    #     pattern = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
    #     if re.search(pattern,email):
    #         return True
    #     else:
    #         return False

    # ## PASSWORD VALIDATION
    # def password_is_valid(password):
    #     if password[0].isupper() or password[0].isnumeric():
    #         if len(password)>=8:
    #             return True
        
    def post(self,request):
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_password')
        if len(firstname)!=0 and len(lastname)!=0 and len(user_name)!=0 and len(email)!=0 and len(password)!=0 and len(confirm_pass)!=0:
            if not User.objects.filter(username=user_name).exists():
                if password == confirm_pass:
                    user = User.objects.create(first_name=firstname,last_name=lastname,username=user_name,password=make_password(password),email=email)
                    user.save()
                    return redirect('login')
                else:
                    messages.error(request,"Password Doesn't match")
            else:
                messages.info(request,"Username Already Taken")
        else:
            messages.info(request,"All field is required")
        return render(request,'authentication/signup.html')

    
# class CreatePost(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'class/add-blog.html'
#     success_url = "/"


class CreatePost(View):
    def get(self,request):
        if request.user.is_authenticated:
            context = {
                "category" : category_list,
            }
            return render(request,'add-blog.html',context)
        else:
            return redirect('login')
    def post(self,request):
        category = Category.objects.all()
        if request.user.is_authenticated:
            title = request.POST.get('title')
            content = request.POST.get('content')
            image = request.FILES.get('image')
            cat = request.POST.get('cat')
            other_images = request.FILES.getlist('multipleimage')
            cat_check = Category.objects.filter(name=cat)
            if len(title)!=0 and len(content)!=0 and len(image)!=0:
                if cat_check.exists():
                    post = Post.objects.create(category=cat_check.first(),title=title,content=content,post_image=image,user=request.user)
                    post.save()
                    for image in other_images:
                        save_image = Image.objects.create(post=post,image=image)
                        save_image.save()
                    messages.success(request,"Your Post has been Successfully Added")
                    return redirect('home')
                else:
                    cats = Category.objects.create(name=cat)
                    post = Post.objects.create(category=cats,title=title,content=content,post_image=image,user=request.user)
                    post.save()
                    messages.success(request,"Your Post has been Successfully Added")
            else:
                messages.info(request,"This Field is Required")
        else:
            return redirect('login')
        context = {
            "category" : category,
        }
        return render(request,'add-blog.html',context)
    

class DeletePost(DeleteView):
    model = Post
    success_url = '/blog/create'

class PostComment(View):
    def post(self,request,id):
        if request.user.is_authenticated:
            if request.user is not None: 
                post = Post.objects.get(id=id)
                user = request.user
                comment = request.POST.get('comment')
                Comment.objects.create(user=user,post=post,comment=comment).save()
                return redirect(f'/blog/post/{post.id}')
            else:
                return redirect('login')
        else:
            return redirect('login')
            
class Login(View):
    def get(self,request):
        context = {
            "category":category_list
        }
        return render(request,"authentication/login.html",context)
    def post(self,request):
        print(request.POST)
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=user_name).exists():
            user = User.objects.get(username=user_name)
            password_check = check_password(password,user.password)
            if password_check:
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                request.session['user_username'] = user.username
                auth.login(request,user)
                return redirect(f'/user/{user.id}/profile')
            else:
                messages.warning(request,"Invalid Username or Password")
        else:
            messages.info(request,"Username doesn't exitst")
        return render(request,"authentication/login.html")
    
class Logout(View):
    def get(self,request):
        auth.logout(request)
        return redirect('login')

class PostByCategory(View):
    def get(self,request,category):
        category = Category.objects.filter(name=category)
        context = {
            "cat":category
        }
        return render(request,'filter-post.html',context)
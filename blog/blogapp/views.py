from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect, render
from .models import Image, Post , Category, Profile,Comment
import re
##  GLOBAL VARIABLE
category_list = Category.objects.select_related()

def home(request):
    post = Post.objects.all().order_by('-published_date')
    category_id = request.GET.get('category')
    search = request.GET.get('search')
    if request.method == "GET":
        if search:
            post = Post.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))
    if category_id:
        post = Post.objects.filter(category=category_id) 
    # post_per_page = 3
    # paginator = Paginator(post,post_per_page)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        "posts":post,
        "category":category_list,
        # "page":page_obj,
        # "paginator":paginator
    }
    return render(request , "index.html", context)

def blog_detail(request,post_id):
    post_detail = Post.objects.get(id=post_id)
    comment = Comment.objects.filter(post=post_detail).order_by('-upload_on')
    context = {
        "post" : post_detail,
        "comments":comment,
        "category":category_list
    }
    return render(request,'blog_detail.html',context)

## PROFILE

def profile(request,username):
    user_detail = User.objects.get(id=username)
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

## ATUHENTICATION 

def login(request):
    if request.method == "POST":
        print(request.POST)
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=user_name).exists():
            user = User.objects.get(username=user_name)
            password_check = check_password(password,user.password)
            if password_check:
                auth.login(request,user)
                return redirect(f'/user/{user.id}/profile')
            else:
                messages.warning(request,"Invalid Username or Password")
        else:
            messages.info(request,"Username doesn't exitst")
    context = {
        "category":category_list
    }
    return render(request , 'authentication/login.html',context)

## EMAIL VALIDATION
def email_validation(email):
    pattern = '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(pattern,email):
        return True
    else:
        return False
        
def signup(request):
    if request.method == "POST":
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_password')
        if len(firstname)!=0 and len(lastname)!=0 and len(user_name)!=0 and len(email)!=0 and len(password)!=0 and len(confirm_pass)!=0:
            if email_validation(email):
                if len(password)>8 :
                    if not User.objects.filter(username=user_name).exists():
                        if password == confirm_pass:
                            user = User.objects.create(first_name=firstname,last_name=lastname,username=user_name,password=make_password(password),email=email)
                            user.save()
                            messages.success(request,"User Created SuccessFully")
                        else:
                            messages.info(request,"Password Doesn't match")
                    else:
                        messages.info(request,"Username Already Taken")
                else:
                    print(0)
            else:
                messages.warning(request,"Invalid Email Adress !!")
        else:
            messages.info(request,"All field is required")
    context = {
        "category":category_list
    }
    return render(request,'authentication/signup.html',context)

@receiver(post_save,sender = User)
def Prof(sender , instance , created , **kwargs):
    if created:
        prof = Profile.objects.create(user=instance)
        prof.save()


def logout(request):
    auth.logout(request)
    return redirect('login')

def post_by_category(request,category):
    category = Category.objects.filter(name=category)
    context = {
        "cat":category
    }
    return render(request,'filter-post.html',context)

## ADD BLOG

def add_blog(request):
    category = Category.objects.all()
    if request.user.is_authenticated:
        if request.method == "POST":
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

def delete_blog(request,id):
    post = Post.objects.filter(id=id)
    post.delete()
    return redirect(f'/user/{request.user.id}/profile')


def post_comment(request,id):
    if request.method == "POST":
        if request.user is not None: 
            post = Post.objects.get(id=id)
            user = request.user
            comment = request.POST.get('comment')
            Comment.objects.create(user=user,post=post,comment=comment).save()
            return redirect(f'/blog/post/{post.id}')
        else:
            return redirect('login')
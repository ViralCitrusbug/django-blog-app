from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.shortcuts import render,redirect
from django.views.generic.base import View

from ..mixin import LoginRequiredMixin

class LoginView(View,LoginRequiredMixin):
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.get(username=username)
        if user.is_superuser:
            password_check = check_password(password,user.password)
            if password_check:
                auth.login(request,user)
                print("YOU ARE LOGGED IN")
                return redirect('index')
            else:
                messages.warning(request,"you are Not ")
        else:
            messages.warning(request,"you are Not SuperUser")
        return render(request,"auth/custom-admin-login.html")
    def get(self,request):
        return render(request,'auth/custom-admin-login.html')
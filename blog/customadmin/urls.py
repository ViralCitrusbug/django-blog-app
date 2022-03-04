from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('custom-admin/user/login',views.LoginView.as_view(),name="custom-admin-login"),
    path('users/',views.UserList.as_view(),name="users")
]
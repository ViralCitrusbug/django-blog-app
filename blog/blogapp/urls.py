from django.urls import path
from . import views,classviews


urlpatterns = [
    # path("",views.home,name="home"),
    # path("blog/post/<int:post_id>",views.blog_detail,name="blog-detail"),
    # path('user/<str:username>/profile',views.profile,name="prfile"),
    path('user/login',views.login,name="login"),
    path('user/logout',views.logout,name="logout"),
    # path('user/create',views.signup,name="register"),
    path('blog/<str:id>/comment',views.post_comment,name='post-comment'),
    path('post/filter/<str:cat>',views.post_by_category,name="post-by-category"),
    path('blog/create',views.add_blog,name='add-blog'),
    path('blog/<str:id>/delete',views.delete_blog,name="delete-blog"),

    ##  CLASS BASED VIEW
    path('',classviews.PostList.as_view(),name="home"),
    path('blog/post/<pk>',classviews.PostDetail.as_view(),name="post-detail"),
    path('user/create',classviews.CreateUser.as_view(),name="create-user"),
    path('user/<int:pk>/profile',classviews.ProfileView.as_view(),name='profile')

]



from msilib.schema import Class
from django.urls import path
from . import views,classviews,serialize_view,serialize_classview,generic_serialize_view


urlpatterns = [
    # path("",views.home,name="home"),
    # path("blog/post/<int:post_id>",views.blog_detail,name="blog-detail"),
    # path('user/<str:username>/profile',views.profile,name="prfile"),
    # path('user/login',views.login,name="login"),
    # path('user/logout',views.logout,name="logout"),
    # path('user/create',views.signup,name="register"),
    # path('blog/<str:id>/comment',views.post_comment,name='post-comment'),
    # path('post/filter/<str:category>',views.post_by_category,name="post-by-category"),
    # path('blog/create',views.add_blog,name='create-blog'),
    # path('blog/<str:id>/delete',views.delete_blog,name="delete-blog"),

    ##  CLASS BASED VIEW

    path('',classviews.PostList.as_view(),name="home"),
    path('blog/post/<int:post_id>',classviews.PostDetail.as_view(),name="post-detail"),
    path('user/create',classviews.CreateUser.as_view(),name="create-user"),
    path('user/<int:pk>/profile',classviews.ProfileView.as_view(),name='profile'),
    path('profile/<int:pk>/update',classviews.ProfileUpdate.as_view()),
    path('blog/<int:pk>/delete',classviews.DeletePost.as_view(),name='delete-blog'),
    path('blog/<str:id>/comment',classviews.PostComment.as_view(),name='post-comment'),
    path('blog/create',classviews.CreatePost.as_view(),name='create-blog'),
    path('user/logout',classviews.Logout.as_view(),name='logout'),
    path('user/login',classviews.Login.as_view(),name='login'),
    path('post/filter/<str:category>',classviews.PostByCategory.as_view(),name="post-by-category"),


    ##  API FUNCTION BASED VIEWS

    # path('api/post-list',serialize_view.post_list,name="api-postlist"),
    # path('api/users',serialize_view.user_list,name="api-user_list"),
    # path('api/user/<pk>',serialize_view.user_crud,name="api-user-crud"),
    # path('api/profile/<pk>',serialize_view.profile_crud,name="api-profile-crud"),

    ## API CLASS BASED VIEWS (CUSTOM VIEWS)
    
    # path('api/post-list',serialize_classview.PostListView.as_view(),name="api-postlist"),
    # path('api/user-list',serialize_classview.UserListView.as_view(),name="api-userlist"),
    # path('api/user/<pk>',serialize_classview.UserCRUD.as_view(),name="api-user-crud"),
    # path('api/profile-list',serialize_classview.ProfileList.as_view(),name="api-profile_list"),
    # path('api/profile/<pk>',serialize_classview.ProfileCRUD.as_view(),name="api-profile-crud"),

    ## API GENERIC CLASS BASED VIEWS

    path('api/post-list',generic_serialize_view.PostListView.as_view(),name="api-postlist"),
    path('api/user-list',generic_serialize_view.UserListView.as_view(),name="api-userlist"),
    path('api/user/<pk>',generic_serialize_view.UserCRUD.as_view(),name="api-user-crud"),
    path('api/profile-list',generic_serialize_view.ProfileListView.as_view(),name="api-profile_list"),
    path('api/profile/<pk>',generic_serialize_view.ProfileCRUD.as_view(),name="api-profile-crud"),
    path('api/post/<pk>',generic_serialize_view.PostCRUD.as_view(),name="api-post-crud"),

]
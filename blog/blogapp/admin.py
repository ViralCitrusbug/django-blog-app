from email.mime import image
from django.contrib import admin
from .models import Post,Category,Profile,Image,Comment


class CatPost(admin.TabularInline):
    model = Post

class PostImage(admin.TabularInline):
    model = Image

class CategoryPost(admin.ModelAdmin):
    inlines = [CatPost]

class HighLightPost(admin.ModelAdmin):
    inlines = [PostImage]

## REGISTERED SITE
admin.site.register(Category,CategoryPost)
admin.site.register(Post,HighLightPost)
admin.site.register(Profile)
admin.site.register(Comment)
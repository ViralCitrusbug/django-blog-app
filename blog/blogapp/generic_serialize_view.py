from rest_framework import mixins,generics
from .models import Post,Profile
from . serializers import PostSerializers, ProfileSerializer, UserSerializer
from django.contrib.auth.models import User

from blogapp import serializers

class PostListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get(self,request):
        return  self.list(request)
    
    def post(self,request):
        # request.data['user'] = request.user.id
        return self.create(request)

class UserListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class UserCRUD(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self,request,pk):
        return self.retrieve(request)

    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        return self.destroy(request)

class ProfileListView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def get(self,request):
        return self.list(request)

class ProfileCRUD(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def get(self,request,pk):
        return self.retrieve(request)
    
    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        return self.destroy(request)

class PostCRUD(generics.GenericAPIView,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get(self,request,pk):
        return self.retrieve(request)
    
    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        return self.destroy(request)
from django.http import JsonResponse
from rest_framework import mixins,generics
from .models import Post,Profile
from . serializers import PostSerializers, ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser    
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView


class PostListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = Post.objects.filter(soft_delete=False)
    serializer_class = PostSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self,request):
        category = request.GET.get('category')
        #print(category)
        self.queryset = Post.objects.filter(category__name=category)
        if len(self.queryset) == 0:
            return JsonResponse(f"No Post in {str(category).upper()} Category",safe=False)
        return  self.list(request)
    
    def post(self,request):
        print(request.data)
        print(request.user.id,request.user.username)
        request.data.update({'user':request.user.id})
        print(request.data)
        return self.create(request)

class UserListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)

class UserCRUD(mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self,request,pk):
        return self.retrieve(request)

    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        return self.destroy(request)

class ProfileListView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
        return self.list(request)

class ProfileCRUD(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = ProfileSerializer
    def get(self,request,pk):
        return self.retrieve(request)
    
    def put(self,request,pk):
        return self.update(request)
    
    #  def delete(self,request,pk):
    #      return self.destroy(request)

class PostCRUD(generics.GenericAPIView,mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get_post(self,pk):
        try:
            post = Post.objects.get(pk=pk)
            return post
        except Post.DoesNotExist:
            return False

    def get(self,request,pk):
        if self.get_post(pk):
            post = Post.objects.get(pk=pk)
            return self.retrieve(request)
        else:
            return JsonResponse("Post Not Found")

    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        post = Post.objects.filter(pk=pk)
        post.update(soft_delete=True)
        return self.retrieve(request)
        

class PostSearchFilter(ListAPIView):
    queryset = Post.objects.filter(soft_delete=False)
    filter_backends = [SearchFilter]
    search_fields = ['content','title']
from blogapp import serialize_view
from .models import Post,Profile
from django.contrib.auth.models import User
from .serializers import UserSerializer,PostSerializers,ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class PostListView(APIView):
    def get(self,request):
        post = Post.objects.all()
        serialize = PostSerializers(post,many=True)
        return Response(serialize.data)
    
    def post(self,request):
        serialize = PostSerializers(data=request.data)
        if serialize.is_valid():
            # print(serialize.validated_data)
            return Response(serialize.data)
        else:
            return Response(serialize.errors)

class UserListView(APIView):
    def get(self,request):
        user = User.objects.all()
        serialize = UserSerializer(user,many=True)
        return Response(serialize.data)
    
    def post(self,request):
        serialize = UserSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)

class UserCRUD(APIView):
    def get_user(self,pk):
        try:
            user = User.objects.get(pk=pk)
            return user
        except User.DoesNotExist:
            return False
    
    def get(self,request,pk):
        if self.get_user(pk):
            serialize = UserSerializer(self.get_user(pk))
            return Response(serialize.data)
        else:
            return Response("User Doesn't Exist")
    def put(self,request,pk):
        serialize = UserSerializer(self.get_user(pk),data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
    
class ProfileList(APIView):
    def get(self,request):
        profile = Profile.objects.all()
        serialize = ProfileSerializer(profile,many=True)
        return Response(serialize.data)

class ProfileCRUD(APIView):
    def get_profile(self,pk):
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
             return False
    
    def get(self,request,pk):
        if self.get_profile(pk):
            serialize = ProfileSerializer(self.get_profile(pk))
            return Response(serialize.data)
        else:
            return Response("Profile doesn't Exist")
    
    def put(self,request,pk):
        if self.get_profile(pk):
            response = request.data
            serialize = ProfileSerializer(self.get_profile(pk),data=response)
            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data)
            else:
                return Response(serialize.errors)
        else:
            return Response("Profile Doesn't Exist")
            
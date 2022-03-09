from .models import Post,Profile
from django.contrib.auth.models import User
from .serializers import PostSerializers, ProfileSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET',"POST"])
def post_list(request):
    if request.method == "GET":
        post = Post.objects.all()
        serializer = PostSerializers(post,many=True)
        response = {
            'serializer':serializer.data
        }
        return Response(response)

    if request.method == "POST":
        serializer = PostSerializers(data=request.data,files=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET',"POST"])
def user_list(request):
    if request.method == "GET":
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        respose = {
            'serializer':serializer.data
        }
        return Response(respose)
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET',"POST"])
def profile_list(request):
    if request.method == "GET":
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile,many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','DELET',"PUT"])
def user_crud(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist :
        return Response("User Doesn't Exist")
    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == "DELETE":
        user.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    if request.method == "PUT":
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET','POST',"PUT","DELETE"])
def profile_crud(request,pk):
    try:
        profile = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response("Profile Doesn't Exist")
    
    if request.method == "GET":
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    if request.method == "DELETE":
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == "PUT":
        serializer = ProfileSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
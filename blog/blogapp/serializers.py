from distutils.file_util import write_file
from rest_framework import serializers
from . models import Post, Profile,User,Category

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields='__all__'
    def create(self, validated_data):
        return Post.objects.create(validated_data)

    def update(self, instance, validated_data):
        new_post = Post(**validated_data)
        new_post.id = instance.id
        new_post.save()
        return new_post





class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, user, validated_data):
        new_user = User(**validated_data)
        new_user.id = user.id
        new_user.save()
        return new_user


# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     username = serializers.CharField()
#     email = serializers.EmailField()
    
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

#     def update(self, user, validated_data):
#         new_user = User(**validated_data)
#         new_user.id = user.id
#         new_user.save()
#         return new_user

        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def create(self, validated_data):
        return super().create(**validated_data)  

    def update(self, profile, validated_data):
        new_profile = Profile(**validated_data)
        new_profile.id = profile.id
        new_profile.save()
        return new_profile
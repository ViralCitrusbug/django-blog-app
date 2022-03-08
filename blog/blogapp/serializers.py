from rest_framework import serializers
from . models import Post, Profile,User,Category

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields='__all__'

        
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"

#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

#     def update(self, user, validated_data):
#         new_user = User(**validated_data)
#         new_user.id = user.id
#         new_user.save()
#         return new_user


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, user, validated_data):
        new_user = User(**validated_data)
        new_user.id = user.id
        new_user.save()
        return new_user

        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def create(self, validated_data):
        return super().create(**validated_data)  

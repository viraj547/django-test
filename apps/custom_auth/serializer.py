from rest_framework import serializers
from apps.custom_auth.models import CustomUser


class LoginUserSerializer(serializers.Serializer):
    email =serializers.EmailField(required=True)
    password = serializers.CharField(required=True,min_length=4,max_length=40)


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id','category','title','description','price','status','created_at','updated_at']



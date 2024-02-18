from rest_framework import serializers
from django.contrib.auth import get_user_model
User=get_user_model()
from random import randint

class UserSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()
    confirm_password=serializers.CharField()
    
    # def validate_password(self,value):
    #     if len(value) < 8:
    #         raise serializers.ValidationError(
    #             "The password must be greater than 8 character"
    #         )
    #     return value

    def validate_email(self,value):
        user=User.objects.filter(email=value).exists()
        if user:
            raise serializers.ValidationError("This email is already in use")
        return value


    def validate(self, attrs):
        if attrs.get('password')!= attrs.get('confirm_password'):
            raise serializers.ValidationError({
                'details':"The password and confirm password must be matched"
            })
        return super().validate(attrs)
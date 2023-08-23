# from rest_framework import serializers
# from .models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['phone_number' , 'password', 'is_verified']

# class VerifyaccountSerializer(serializers.Serializer):
#     phone_number=serializers.EmailField()
#     otp=serializers.CharField()
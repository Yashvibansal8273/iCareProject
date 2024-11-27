from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(max_length=15, required=True)
    password = serializers.CharField(max_length=128, required=True)

    def validate(self, data):
        user = authenticate(username=data.get('mobile_number'), password=data.get('password'))
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user

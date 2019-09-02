from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password_hash = serializers.CharField(max_length=255)

class Login():
    def TryLogin(s):
        return True
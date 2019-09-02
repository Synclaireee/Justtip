from rest_framework import serializers
from regtest.models import UserTest

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password_hash = serializers.CharField(max_length=255)

class Login():
    
    def TryLogin(s):
        userstring = s['username']
        password_hash_string = s['password_hash']
        try:
            UserTest.objects.get(username=userstring, password_hash=password_hash_string)
        except UserTest.DoesNotExist:
            return False
        return True
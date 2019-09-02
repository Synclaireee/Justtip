from rest_framework import serializers
from regtest.models import UserTest
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserTest
        fields = ['id', 'created', 'username', 'password_hash', 'email', 'phone_number', 'first_name', 'last_name', 'description', 'verification_status']
        validators = UniqueTogetherValidator(
            queryset = UserTest.objects.all(),
            fields = ['username','email','phone_number']
        )

    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField()
    username = serializers.CharField(max_length=255)
    password_hash = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    verification_status = serializers.CharField(max_length=255)
    profile_picture = serializers.CharField(max_length=None)

    def create(self, validated_data):
        return TestEndpoint.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.password_hash = validated_data.get('password_hash', instance.password_hash)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.description = validated_data.get('description', instance.description)
        instance.verification_status = validated_data.get('verification_status', instance.verification_status)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.save()
        return instance
from rest_framework import serializers
from testEndPoint.models import TestEndpoint


class SnippetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TestEndpoint
        fields = ['id', 'title', 'text1', 'bool1', 'int1']

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    text1 = serializers.CharField()
    bool1 = serializers.BooleanField()
    int1 = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return TestEndpoint.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.text1 = validated_data.get('text1', instance.text1)
        instance.bool1 = validated_data.get('bool1', instance.bool1)
        instance.int1 = validated_data.get('int1', instance.int1)
        instance.save()
        return instance
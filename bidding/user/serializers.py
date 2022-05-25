from rest_framework import serializers


class UserCreateAPIViewInputSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=40)
    email = serializers.EmailField(max_length=255, required=False)
    first_name = serializers.CharField(max_length=60, required=False)
    last_name = serializers.CharField(max_length=60, required=False)
    is_superuser = serializers.BooleanField(default=False)
    password = serializers.CharField()


class UserCreateAPIViewOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    username = serializers.CharField()
    email = serializers.EmailField(allow_null=True)
    first_name = serializers.CharField(allow_null=True)
    last_name = serializers.CharField(allow_null=True)
    is_active = serializers.BooleanField()
    is_email_verified = serializers.BooleanField()
    is_superuser = serializers.BooleanField()
    created = serializers.DateTimeField()

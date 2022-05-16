from rest_framework import serializers


class UserAuthInputSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserAuthOutputSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


class UserAuthRefreshInputSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class UserAuthRefreshOutputSerializer(serializers.Serializer):
    access = serializers.CharField()

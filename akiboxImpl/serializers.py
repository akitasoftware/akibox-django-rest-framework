from akiboxImpl.models import User, File
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone']


class FileSerializer(serializers.Serializer):
    class Meta:
        model = File
        fields = ['id', 'created_at', 'contents']


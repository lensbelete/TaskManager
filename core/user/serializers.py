from rest_framework import serializers
from core.user.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model =User
        fields = ['id', 'email', 'first_name', 'last_name','username','created', 'updated']
        # read_only_fields = ['is_active']

from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    serializer to handle turning our `User` object into
    something that can be JSONified and sent to the client
    """
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        """
        Function is used to create user object with serializer.
        :param validated_data: keep all user related data.
        :return: user object.
        """
        user = User.objects.create_user(**validated_data)
        return user

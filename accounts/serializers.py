from accounts.models import User
from rest_framework.serializers import ModelSerializer, CharField


class UserSerializer(ModelSerializer):

    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
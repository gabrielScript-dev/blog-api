from accounts.models import User
from blog.models import Author
from blog.serializers import AuthorSerializer
from rest_framework.serializers import ModelSerializer, CharField
from django.db import transaction


class UserSerializer(ModelSerializer):

    author = AuthorSerializer(write_only=True)
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'author', 'email', 'password']

    def create(self, validated_data):

        author_data = validated_data.pop('author')

        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            Author.objects.create(user=user, **author_data)

        return user
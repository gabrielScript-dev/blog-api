from blog.models import Author, Post
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, DateTimeField


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'date_of_birth']


class PostSerializer(ModelSerializer):

    created_at = DateTimeField(read_only=True)
    author = PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Post
        fields = ['title', 'author', 'text', 'created_at']